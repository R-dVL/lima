"""
Views for the 'Inventory' app.

This module handles the logic for managing articles in the inventory.
"""
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .forms import ArticleForm
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
    # Retrieve all articles from the inventory
    items = Article.objects.all()  # pylint: disable=E1101
    # Calculate the total price of all articles (price * quantity)
    total_price = sum(item.price * item.quantity for item in items)
    return render(request, 'article_list.html', {'items': items, 'total_price': total_price})

@login_required
def increase_quantity(request, pk):
    """
    Increase the quantity of an article in the inventory.

    Args:
        request: The HTTP request object.
        pk: The primary key of the article to increase.

    Returns:
        Redirects to the article list page.
    """
    # Retrieve the article using the primary key (pk)
    item = get_object_or_404(Article, pk=pk)
    # Increase the article's quantity by 1
    item.increase_quantity(1)
    return redirect('article_list')

@login_required
def decrease_quantity(request, pk):
    """
    Decrease the quantity of an article in the inventory.

    Args:
        request: The HTTP request object.
        pk: The primary key of the article to decrease.

    Returns:
        Redirects to the article list page.
    """
    # Retrieve the article using the primary key (pk)
    item = get_object_or_404(Article, pk=pk)
    # Decrease the article's quantity by 1
    item.decrease_quantity(1)
    return redirect('article_list')

## CRUD ##
# Create
# pylint: disable=R0901
class ArticleCreateView(CreateView):
    """
    Create Article form model.
    """
    model = Article
    template_name = 'crud/create_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')

# Update
class ArticleUpdateView(UpdateView):
    """
    Update Article form model.
    """
    model = Article
    template_name = 'crud/update_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')

# Read
class ArticleReadView(DetailView):
    """
    Read Article form model.
    """
    model = Article
    template_name = 'crud/read_article.html'

# Delete
class ArticleDeleteView(DeleteView):
    """
    Delete Article form model.
    """
    model = Article
    template_name = 'crud/delete_article.html'
    success_url = reverse_lazy('article_list')