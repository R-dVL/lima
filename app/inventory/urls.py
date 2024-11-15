"""
Defines URL patterns for the 'article' application.

This module maps URL paths to corresponding views in the 'article' app.
Each path function takes a URL pattern, a view to be called, and an optional name.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('increase/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),
    path('create/', views.ArticleCreateView.as_view(), name='create_article'),
    path('update/<int:pk>', views.ArticleUpdateView.as_view(), name='update_article'),
    path('read/<int:pk>', views.ArticleReadView.as_view(), name='read_article'),
    path('delete/<int:pk>', views.ArticleDeleteView.as_view(), name='delete_article')
]
