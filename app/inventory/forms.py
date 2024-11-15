"""
CRUD Forms for 'inventory' app
"""
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Item, List

class ListForm(forms.ModelForm):
    """
    Form for adding or editing an list in the inventory.
    """
    class Meta:
        """
        Meta
        """
        model = Item
        fields = ['name', 'description']

        labels = {
            'name': _('Name'),
            'description': _('Description')
        }

class ItemForm(forms.ModelForm):
    """
    Form for adding or editing an item in the inventory.
    """
    class Meta:
        """
        Meta
        """
        model = Item
        fields = ['name', 'description', 'price', 'amount', 'amount_to_buy']

        widgets = {
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': _('Per unit'),
                'min': '0',
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': _('Units'),
                'min': '0',
            }),
        }

        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'price': _('Price'),
            'amount': _('Amount'),
            'amount_to_buy': _('Amount to buy')
        }
