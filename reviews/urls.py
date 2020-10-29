from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('p=<int:page>', views.index, name='page'),
    path('p=<int:page>&q=<q>', views.index, name='query_page'),
    path('/<int:category>', views.category, name='category'),
    path('/<int:category>/p=<int:page>', views.category, name='category_page'),
]
