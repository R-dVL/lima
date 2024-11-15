"""
CRUD Forms for 'inventory' app
"""
from django import forms

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
                'placeholder': 'Por unidad',
                'min': '0',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Unidades',
                'min': '0',
            }),
        }

        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'quantity': 'Cantidad',
            'quantity_to_buy': 'Cantidad a comprar'
        }

class ItemFilterForm(forms.Form):
    """
    Searchbar form configuration
    """
    name = forms.CharField(
        required=False,
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por nombre'
            }
        )
    )
