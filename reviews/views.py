from math import ceil

from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse

from .models import Review, Category, Comment


ELEMENT_IN_PAGE = 5


def index(request, page=1, q=''):
    if request.method == 'POST':
        q = request.POST['query']
        reviews = Review.objects.filter(title__icontains=q).order_by('-id')
    elif q:
        reviews = Review.objects.filter(title__icontains=q).order_by('-id')
    else:
        reviews = Review.objects.order_by('-id')

    categories = Category.objects.all()
    count_pages = ceil(len(reviews) / ELEMENT_IN_PAGE)
    reviews = reviews[(page - 1) * ELEMENT_IN_PAGE:page * ELEMENT_IN_PAGE]
    return render(request, 'index.html', {
        'reviews': reviews,
        'categories': categories,
        'pages': range(1, count_pages + 1) if count_pages > 1 else False,
        'query': q,
    })


def category(request, pk, page=1):
    reviews = Review.objects.filter(category_id=pk).order_by('-id')

    categories = Category.objects.all()
    count_pages = ceil(len(reviews) / ELEMENT_IN_PAGE)
    reviews = reviews[(page - 1) * ELEMENT_IN_PAGE:page * ELEMENT_IN_PAGE]
    return render(request, 'index.html', {
        'reviews': reviews,
        'categories': categories,
        'category': categories.get(id=pk),
        'pages': range(1, count_pages + 1) if count_pages > 1 else False,
    })


def review(request, pk):
    if request.method == 'POST':  # Post comment
        try:
            Comment(review_id=pk, stars=request.POST['stars'],
                    content=request.POST['content'],
                    author=request.POST['author']).save()
        except:
            return HttpResponseBadRequest
        return HttpResponseRedirect(reverse('review',  args=(pk,)))

    rev = Review.objects.get(id=pk)
    comments = Comment.objects.filter(review=rev).order_by('-id')[:5]

    return render(request, 'review.html', {
        'rev': rev,
        'comments': comments,
    })
