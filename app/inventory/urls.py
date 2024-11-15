"""
Defines URL patterns for the 'item' application.

This module maps URL paths to corresponding views in the 'item' app.
Each path function takes a URL pattern, a view to be called, and an optional name.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lists, name='lists'),
    path('item/increase/<int:pk>/', views.increase_amount, name='increase_amount'),
    path('item/decrease/<int:pk>/', views.decrease_amount, name='decrease_amount'),
    path('item/create/<int:pk>/', views.ItemCreateView.as_view(), name='create_item'),
    path('item/update/<int:pk>', views.ItemUpdateView.as_view(), name='update_item'),
    path('item/read/<int:pk>', views.ItemReadView.as_view(), name='read_item'),
    path('item/delete/<int:pk>', views.ItemDeleteView.as_view(), name='delete_item'),
    path('lists/', views.lists, name='lists'),
    path('lists/<int:pk>/', views.list_detail, name='list_detail')
]
