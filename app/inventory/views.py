"""
Views for the 'Inventory' app.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article

@login_required
def article_list(request):
    """
    Render the list of articles in the inventory.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML page displaying the list of articles.
    """
    items = Article.objects.all()  # Ensure that the Article model has the default manager
    return render(request, 'article_list.html', {'items': items})

@login_required
def increase_quantity(request, pk):
    """
    Increase the quantity of an article at home.

    Args:
        request: The HTTP request object.
        pk: The primary key of the article to increase.

    Returns:
        Redirects to the article list page.
    """
    item = get_object_or_404(Article, pk=pk)
    item.increase_quantity(1)
    return redirect('article_list')

@login_required
def decrease_quantity(request, pk):
    """
    Decrease the quantity of an article at home.

    Args:
        request: The HTTP request object.
        pk: The primary key of the article to decrease.

    Returns:
        Redirects to the article list page.
    """
    item = get_object_or_404(Article, pk=pk)
    item.decrease_quantity(1)
    return redirect('article_list')

@login_required
def increase_quantity_to_buy(request, pk):
    """
    Increase the quantity of an article to buy.

    Args:
        request: The HTTP request object.
        pk: The primary key of the article to increase to buy.

    Returns:
        Redirects to the article list page.
    """
    item = get_object_or_404(Article, pk=pk)
    item.add_to_buy(1)
    return redirect('article_list')

@login_required
def decrease_quantity_to_buy(request, pk):
    """
    Decrease the quantity of an article to buy.

    Args:
        request: The HTTP request object.
        pk: The primary key of the article to decrease to buy.

    Returns:
        Redirects to the article list page.
    """
    item = get_object_or_404(Article, pk=pk)
    item.remove_from_buy(1)
    return redirect('article_list')
