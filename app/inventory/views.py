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
    Redirects any request to /inventory/lists/
    """
    return redirect('/inventory/lists/')

@login_required
def lists(request):
    """
    Render the list of lists, with links to the item list of each list.
    """
    lists = List.objects.all()

    return render(request, 'lists.html', {'lists': lists})

@login_required
def list_detail(request, pk):
    """
    Render the list of items in the selected list.
    """
    list_obj = get_object_or_404(List, pk=pk)
    items = list_obj.items.all()

    # Calculate the total global cost for the items in this list
    total_global_cost = sum(item.total_cost() for item in items)

    return render(request, 'list_detail.html', {
        'list': list_obj,
        'items': items,
        'total_global_cost': total_global_cost,
    })

@login_required
def increase_amount(request, pk):
    """
    Increase the amount of an item in the inventory.
    """
    item = get_object_or_404(Item, pk=pk)
    list_pk = item.list.pk  # Get the List associated with the item
    item.increase_amount(1)
    return redirect('list_detail', pk=list_pk)

@login_required
def decrease_amount(request, pk):
    """
    Decrease the amount of an item in the inventory.
    """
    item = get_object_or_404(Item, pk=pk)
    list_pk = item.list.pk  # Get the List associated with the item
    item.decrease_amount(1)
    return redirect('list_detail', pk=list_pk)

## CRUD ##
# Create
# pylint: disable=R0901
class ItemCreateView(CreateView):
    """
    Create a new Item for a specific Inventory List.
    """
    model = Item
    template_name = 'crud/create_item.html'
    form_class = ItemForm

    def form_valid(self, form):
        # Get the List object based on the 'pk' from the URL
        list_pk = self.kwargs.get('pk')  # Retrieve the list_pk from URL kwargs
        inventory_list = get_object_or_404(List, pk=list_pk)

        # Assign the inventory list to the new Item instance
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
class ItemReadView(DetailView):
    """
    Read Item form model.
    """
    model = Item
    template_name = 'crud/read_item.html'

# Update
class ItemUpdateView(UpdateView):
    """
    Update Item form model.
    """
    model = Item
    template_name = 'crud/update_item.html'
    form_class = ItemForm

    def form_valid(self, form):
        # Save the form and update the item
        item = form.save()

        # Get the list_pk from the form
        list_pk = self.request.POST.get('list_pk')  # Get the list's primary key from the form

        # Redirect to the list_detail view for the relevant list
        return redirect('list_detail', pk=list_pk)

    def get_success_url(self):
        # Optionally, you can use this method to specify the redirect URL
        list_pk = self.object.list.pk
        return reverse_lazy('list_detail', kwargs={'pk': list_pk})

# Delete
class ItemDeleteView(DeleteView):
    """
    Delete Item form model.
    """
    model = Item
    template_name = 'crud/delete_item.html'

    def get_success_url(self):
        # Redirect to the list_detail view of the List this item belongs to
        list_pk = self.object.list.pk  # Get the List object from the deleted Item
        return reverse_lazy('list_detail', kwargs={'pk': list_pk})

class ListCreateView(CreateView):
    """
    Create a new Inventory List.
    """
    model = List
    template_name = 'crud/create_list.html'
    form_class = ListForm

    def form_valid(self, form):
        # Save the form and redirect to the list detail view
        self.object = form.save()
        return redirect('list_detail', pk=self.object.pk)

class ListUpdateView(UpdateView):
    """
    Update an Inventory List.
    """
    model = List
    template_name = 'crud/update_list.html'
    form_class = ListForm

    def form_valid(self, form):
        # Save the updated list
        self.object = form.save()
        return redirect('list_detail', pk=self.object.pk)

    def get_success_url(self):
        # Optionally specify the redirect URL
        return reverse_lazy('list_detail', kwargs={'pk': self.object.pk})

class ListDeleteView(DeleteView):
    """
    Delete an Inventory List.
    """
    model = List
    template_name = 'crud/delete_list.html'

    def get_success_url(self):
        # Redirect to the main list overview page after deletion
        return reverse_lazy('lists')
