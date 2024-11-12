"""
Defines URL patterns for the 'article' application.

This module maps URL paths to corresponding views in the 'article' app.
Each path function takes a URL pattern, a view to be called, and an optional name.

Routes:
    '' : Maps the root URL of the app to the 'index' view.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('add/', views.add_article, name='add_article'),
    path('increase/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),
    path('delete/<int:pk>/', views.delete_article, name='delete_article'),
]
