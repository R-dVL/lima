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
    path('increase/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),
    path(
        'increase-to-buy/<int:pk>/',
        views.increase_quantity_to_buy,
        name='increase_quantity_to_buy'
        ),
    path(
        'decrease-to-buy/<int:pk>/',
        views.decrease_quantity_to_buy,
        name='decrease_quantity_to_buy'
    ),
]
