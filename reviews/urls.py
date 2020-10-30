from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('p=<int:page>', views.index, name='page'),
    path('p=<int:page>&q=<q>', views.index, name='query_page'),
    path('category/<int:pk>', views.category, name='category'),
    path('category/<int:pk>/p=<int:page>', views.category, name='category_page'),
    path('review/<int:pk>', views.review, name='review'),
    path('new_review', views.new_review, name='new_review'),
]
