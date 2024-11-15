"""
CRUD Forms for 'inventory' app
"""
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Article

class ArticleForm(forms.ModelForm):
    """
    Form for adding or editing an article in the inventory.
    """
    class Meta:
        """
        Meta
        """
        model = Article
        fields = ['name', 'description', 'price', 'quantity', 'quantity_to_buy']

        widgets = {
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': _('Per unit'),
                'min': '0',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': _('Units'),
                'min': '0',
            }),
        }

        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'price': _('Price'),
            'quantity': _('Amount'),
            'quantity_to_buy': _('Amount to buy')
        }
