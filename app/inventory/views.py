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

class ArticleForm(forms.ModelForm):
    """
    Form for adding or editing an article in the inventory.

    Inherits from Django's ModelForm to generate a form based on the Article model.
    """
    class Meta:
        model = Article
        fields = ['name', 'description', 'price', 'quantity']

@login_required
def add_article(request):
    """
    Handle the addition of a new article to the inventory.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML page for adding a new article or redirects to the article list upon success.
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # If the form is valid, save the article and redirect to the article list
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()  # Display an empty form for adding an article
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
    # Retrieve the article using the primary key (pk)
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == 'POST':
        # If the form is submitted, delete the article
        article.delete()
        return redirect('article_list')
    
    # If the method is GET, display the delete confirmation page
    return render(request, 'delete_article.html', {'article': article})
