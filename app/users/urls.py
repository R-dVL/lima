"""
URL configuration for the 'users' app.

This module defines the URL patterns related to user authentication, including
the login and logout views.

Routes:
    - 'login/': Maps to the login view.
    - 'logout/': Maps to the logout view.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Login URL
    path('logout/', views.logout_view, name='logout'),  # Logout URL
]
