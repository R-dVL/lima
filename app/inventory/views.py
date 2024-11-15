"""
Views for the 'Inventory' app.

This module handles the logic for managing articles in the inventory.
"""
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .forms import ArticleForm, ItemFilterForm
from .models import Article

@login_required
def article_list(request):
    """
    Render the list of articles in the inventory with filtering options.
    Automatically sorted by quantity (ascending).
    """
    # Retrieve all articles from the inventory and order them by quantity (ascending)
    articles = Article.objects.all().order_by('quantity')

    # Calculate the total global cost to reach the desired quantity for all items
    total_global_cost = sum(article.total_cost() for article in articles)

    # Article total price to reach desired stock
    total_price = sum(article.price * article.quantity for article in articles)

    # Render the page with the articles, the filter form, and the total global cost
    return render(request, 'article_list.html', {
        'articles': articles,
        'total_price': total_price,
        'total_global_cost': total_global_cost
    })

@login_required
def increase_quantity(request, pk):  # pylint: disable=unused-argument
    """
    Increase the quantity of an article in the inventory.
    """
    # Retrieve the article using the primary key (pk)
    article = get_object_or_404(Article, pk=pk)
    # Increase the article's quantity by 1
    article.increase_quantity(1)
    return redirect('article_list')

@login_required
def decrease_quantity(request, pk):
    """
    Decrease the quantity of an article in the inventory.
    """
    # Retrieve the article using the primary key (pk)
    article = get_object_or_404(Article, pk=pk)
    # Decrease the article's quantity by 1
    article.decrease_quantity(1)
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

# Read
class ArticleReadView(DetailView):
    """
    Read Article form model.
    """
    model = Article
    template_name = 'crud/read_article.html'

# Update
class ArticleUpdateView(UpdateView):
    """
    Update Article form model.
    """
    model = Article
    template_name = 'crud/update_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')

# Delete
class ArticleDeleteView(DeleteView):
    """
    Delete Article form model.
    """
    model = Article
    template_name = 'crud/delete_article.html'
    success_url = reverse_lazy('article_list')
