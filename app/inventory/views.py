"""
Views for the 'Inventory' app.

This module handles the logic for managing items in the inventory.
"""
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .forms import ItemForm, ListForm
from .models import Item, List

def redirect_to_lists(request):
    """
    Redirects any request to /inventory/lists/.
    """
    return redirect('/inventory/lists/')

@login_required
def lists(request):
    """
    Render the list of inventory lists with links to each list's items.
    """
    lists_obj = List.objects.all()
    return render(request, 'lists.html', {'lists': lists_obj})

@login_required
def list_detail(request, pk):
    """
    Render the list of items in a selected inventory list.
    """
    list_obj = get_object_or_404(List, pk=pk)
    items = list_obj.items.all().order_by('amount')

    # Calculate the total global cost for items in the list
    total_global_cost = sum(item.total_cost() for item in items)

    return render(request, 'list_detail.html', {
        'list': list_obj,
        'items': items,
        'total_global_cost': total_global_cost,
    })

@login_required
def increase_amount(request, pk):
    """
    Increase the amount of a specific item in the inventory by 1.
    """
    item = get_object_or_404(Item, pk=pk)
    list_pk = item.list.pk  # Get the associated List's primary key
    item.increase_amount(1)
    return redirect('list_detail', pk=list_pk)

@login_required
def decrease_amount(request, pk):
    """
    Decrease the amount of a specific item in the inventory by 1.
    """
    item = get_object_or_404(Item, pk=pk)
    list_pk = item.list.pk  # Get the associated List's primary key
    item.decrease_amount(1)
    return redirect('list_detail', pk=list_pk)

## CRUD Views for Item ##
class ItemCreateView(CreateView):
    """
    Create a new Item in a specific Inventory List.
    """
    model = Item
    template_name = 'crud/create_item.html'
    form_class = ItemForm

    def form_valid(self, form):
        # Retrieve the List object based on the 'pk' in the URL
        list_pk = self.kwargs.get('pk')
        inventory_list = get_object_or_404(List, pk=list_pk)

        # Assign the List to the new Item
        form.instance.list = inventory_list

        # Save the new item and redirect to the list detail view
        self.object = form.save()
        return redirect('list_detail', pk=list_pk)

    def get_context_data(self, **kwargs):
        # Include the List in the template context
        context = super().get_context_data(**kwargs)
        list_pk = self.kwargs.get('pk')
        context['list'] = get_object_or_404(List, pk=list_pk)
        return context

class ItemReadView(DetailView):
    """
    Display detailed information for an Item.
    """
    model = Item
    template_name = 'crud/read_item.html'

class ItemUpdateView(UpdateView):
    """
    Update an existing Item in the inventory.
    """
    model = Item
    template_name = 'crud/update_item.html'
    form_class = ItemForm

    def form_valid(self, form):
        # Save the updated item
        self.object = form.save()

        # Get the associated List's primary key from the form data
        list_pk = self.request.POST.get('list_pk')

        # Redirect to the list detail view
        return redirect('list_detail', pk=list_pk)

    def get_success_url(self):
        # Redirect to the list detail page after a successful update
        list_pk = self.object.list.pk
        return reverse_lazy('list_detail', kwargs={'pk': list_pk})

class ItemDeleteView(DeleteView):
    """
    Delete an existing Item from the inventory.
    """
    model = Item
    template_name = 'crud/delete_item.html'

    def get_success_url(self):
        # Redirect to the list detail view of the List this item belongs to
        list_pk = self.object.list.pk
        return reverse_lazy('list_detail', kwargs={'pk': list_pk})

## CRUD Views for List ##
class ListCreateView(CreateView):
    """
    Create a new Inventory List.
    """
    model = List
    template_name = 'crud/create_list.html'
    form_class = ListForm

    def form_valid(self, form):
        # Save the new list and redirect to its detail view
        self.object = form.save()
        return redirect('list_detail', pk=self.object.pk)

class ListUpdateView(UpdateView):
    """
    Update an existing Inventory List.
    """
    model = List
    template_name = 'crud/update_list.html'
    form_class = ListForm

    def form_valid(self, form):
        # Save the updated list
        self.object = form.save()
        return redirect('list_detail', pk=self.object.pk)

    def get_success_url(self):
        # Optionally specify the redirect URL after a successful update
        return reverse_lazy('list_detail', kwargs={'pk': self.object.pk})

class ListDeleteView(DeleteView):
    """
    Delete an Inventory List and its associated items.
    """
    model = List
    template_name = 'crud/delete_list.html'

    def get_success_url(self):
        # Redirect to the lists overview page after deletion
        return reverse_lazy('lists')
