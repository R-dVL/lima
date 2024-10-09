"""
Defines URL patterns for the 'inventory' application.

This module maps URL paths to corresponding views in the 'inventory' app.
Each path function takes a URL pattern, a view to be called, and an optional name.

Routes:
    '' : Maps the root URL of the app to the 'index' view.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')  # Root URL mapped to the index view
]
