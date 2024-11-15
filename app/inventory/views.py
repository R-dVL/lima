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
from .models import Article, List

@login_required
def lists(request):
    """
    Render the list of lists, with links to the article list of each list.
    """
    lists = List.objects.all()

    return render(request, 'lists.html', {'lists': lists})

@login_required
def list_detail(request, pk):
    """
    Render the list of articles in the selected list.
    """
    list_obj = get_object_or_404(List, pk=pk)
    articles = list_obj.articles.all()

    # Calculate the total global cost for the articles in this list
    total_global_cost = sum(article.total_cost() for article in articles)

    return render(request, 'list_detail.html', {
        'list': list_obj,
        'articles': articles,
        'total_global_cost': total_global_cost,
    })

@login_required
def increase_quantity(request, pk):
    """
    Increase the quantity of an article in the inventory.
    """
    article = get_object_or_404(Article, pk=pk)
    list_pk = article.list.pk  # Get the List associated with the article
    article.increase_quantity(1)
    return redirect('list_detail', pk=list_pk)

@login_required
def decrease_quantity(request, pk):
    """
    Decrease the quantity of an article in the inventory.
    """
    article = get_object_or_404(Article, pk=pk)
    list_pk = article.list.pk  # Get the List associated with the article
    article.decrease_quantity(1)
    return redirect('list_detail', pk=list_pk)

## CRUD ##
# Create
# pylint: disable=R0901
class ArticleCreateView(CreateView):
    """
    Create a new Article for a specific Inventory List.
    """
    model = Article
    template_name = 'crud/create_article.html'
    form_class = ArticleForm

    def form_valid(self, form):
        # Get the List object based on the 'pk' from the URL
        list_pk = self.kwargs.get('pk')  # Retrieve the list_pk from URL kwargs
        inventory_list = get_object_or_404(List, pk=list_pk)

        # Assign the inventory list to the new Article instance
        form.instance.list = inventory_list  # Ensure the ForeignKey is set

        # Save the form and redirect to the 'list_detail' view
        self.object = form.save()
        return redirect('list_detail', pk=list_pk)

    def get_context_data(self, **kwargs):
        # Include the List object in the template context
        context = super().get_context_data(**kwargs)
        list_pk = self.kwargs.get('pk')
        context['list'] = get_object_or_404(List, pk=list_pk)
        return context


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

    def form_valid(self, form):
        # Save the form and update the article
        article = form.save()

        # Get the list_pk from the form
        list_pk = self.request.POST.get('list_pk')  # Get the list's primary key from the form

        # Redirect to the list_detail view for the relevant list
        return redirect('list_detail', pk=list_pk)

    def get_success_url(self):
        # Optionally, you can use this method to specify the redirect URL
        list_pk = self.object.list.pk
        return reverse_lazy('list_detail', kwargs={'pk': list_pk})

# Delete
class ArticleDeleteView(DeleteView):
    """
    Delete Article form model.
    """
    model = Article
    template_name = 'crud/delete_article.html'

    def get_success_url(self):
        # Redirect to the list_detail view of the List this article belongs to
        list_pk = self.object.list.pk  # Get the List object from the deleted Article
        return reverse_lazy('list_detail', kwargs={'pk': list_pk})
