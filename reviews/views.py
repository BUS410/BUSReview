from math import ceil

from django.shortcuts import render
from django.http import HttpResponseRedirect
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
    reviews = reviews[(page - 1) * ELEMENT_IN_PAGE: page * ELEMENT_IN_PAGE]
    return render(request, 'index.html', {
        'reviews': reviews,
        'categories': categories,
        'category': categories.get(id=pk),
        'pages': range(1, count_pages + 1) if count_pages > 1 else False,
    })


def review(request, pk):
    if request.method == 'POST':
        Comment(review_id=pk, stars=request.POST['stars'],
                content=request.POST['content'],
                author=request.POST['author']).save()
        return HttpResponseRedirect(reverse('review',  args=(pk,)))

    rev = Review.objects.get(id=pk)
    review_comments = Comment.objects.filter(review=rev).order_by('-id')[:5]

    return render(request, 'review.html', {
        'rev': rev,
        'comments': review_comments,
    })


def new_review(request):
    categories = Category.objects.order_by('name')

    if request.method == 'POST':
        if request.POST['category'] == '0':
            current_category = Category(name=request.POST['new_category'])
            current_category.save()
        else:
            current_category = Category.objects.get(id=request.POST['category'])
        rev = Review(title=request.POST['title'],
                     object=request.POST['object'],
                     stars=request.POST['stars'],
                     author=request.POST['author'],
                     content=request.POST['content'],
                     category=current_category)
        if 'image_url' in request.POST:
            rev.image_url = request.POST['image_url']
        rev.save()

        return HttpResponseRedirect(reverse('index'))

    return render(request, 'new_review.html', {
        'categories': categories,
    })


def comments(request, review_id, page=1):
    review_comments = Comment.objects.filter(review_id=review_id).order_by('-id')
    count_pages = ceil(len(review_comments) / ELEMENT_IN_PAGE)
    review_comments = review_comments[(page - 1) * ELEMENT_IN_PAGE: page * ELEMENT_IN_PAGE]
    review = Review.objects.get(id=review_id)
    return render(request, 'comments.html', {
        'review': review,
        'comments': review_comments,
        'pages': range(1, count_pages + 1) if count_pages > 1 else False,
    })
