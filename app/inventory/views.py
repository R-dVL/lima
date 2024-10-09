"""
Views for the 'inventory' app.
"""
from django.shortcuts import render

def index(request):
    """
    View function for the index page.

    This function handles requests to the root URL of the app and returns
    the 'index.html' template as a response.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'index.html' template.
    """
    return render(request, 'index.html')
