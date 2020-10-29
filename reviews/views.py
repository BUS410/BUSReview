from math import ceil

from django.shortcuts import render

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


def category(request, category, page=1):
    reviews = Review.objects.filter(category_id=category).order_by('-id')

    categories = Category.objects.all()
    count_pages = ceil(len(reviews) / ELEMENT_IN_PAGE)
    reviews = reviews[(page - 1) * ELEMENT_IN_PAGE:page * ELEMENT_IN_PAGE]
    return render(request, 'index.html', {
        'reviews': reviews,
        'categories': categories,
        'category': category,
        'pages': range(1, count_pages + 1) if count_pages > 1 else False,
    })
