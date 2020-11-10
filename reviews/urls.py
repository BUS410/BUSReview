from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('p=<int:page>', views.index, name='page'),
    path('p=<int:page>&q=<q>', views.index, name='query_page'),
    path('category/<int:pk>', views.category, name='category'),
    path('category/<int:pk>/p=<int:page>', views.category, name='category_page'),
    path('by_author/<author>', views.reviews_by_author, name='by_author'),
    path('by_author/<author>/p=<int:page>', views.reviews_by_author, name='by_author_page'),
    path('by_object/<review_object>', views.reviews_by_object, name='by_object'),
    path('by_object/<review_object>/p=<int:page>', views.reviews_by_object, name='by_object_page'),
    path('review/<int:pk>', views.review, name='review'),
    path('new_review', views.new_review, name='new_review'),
    path('comments/<int:review_id>/', views.comments, name='comments'),
    path('comments/<int:review_id>/p=<int:page>', views.comments, name='comments_page'),
]
