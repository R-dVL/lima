"""
Views for the 'Inventory' app.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article

@login_required
def article_list(request):
    items = Article.objects.all()
    return render(request, 'article_list.html', {'items': items})

# Views for 'at home' quantity
def increase_quantity(request, pk):
    item = get_object_or_404(Article, pk=pk)
    item.increase_quantity(1)
    return redirect('article_list')

def decrease_quantity(request, pk):
    item = get_object_or_404(Article, pk=pk)
    item.decrease_quantity(1)
    return redirect('article_list')

# Views for 'to buy' quantity
def increase_quantity_to_buy(request, pk):
    item = get_object_or_404(Article, pk=pk)
    item.add_to_buy(1)
    return redirect('article_list')

def decrease_quantity_to_buy(request, pk):
    item = get_object_or_404(Article, pk=pk)
    item.remove_from_buy(1)
    return redirect('article_list')
