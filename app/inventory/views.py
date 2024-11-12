"""
Views for the 'Inventory' app.

This module handles the logic for managing articles in the inventory.
"""
from django import forms
from django.urls import reverse
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
    items = Article.objects.all()  # pylint: disable=E1101
    return render(request, 'article_list.html', {'items': items})

@login_required
def increase_quantity(request, pk):  # pylint: disable=unused-argument
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
def decrease_quantity(request, pk):  # pylint: disable=unused-argument
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

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'quantity']

@login_required
def add_article(request):
    """
    Handle the addition of a new article to the inventory.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML page for adding a new article or redirects to the article list.
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})

@login_required
def delete_article(request, pk):
    """
    Handle the deletion of an article from the inventory.

    Args:
        request: The HTTP request object.
        pk: The primary key of the article to delete.

    Returns:
        Redirects to the article list page upon successful deletion.
    """
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    
    return render(request, 'delete_article.html', {'article': article})
