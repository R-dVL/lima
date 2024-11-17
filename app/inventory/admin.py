"""
Admin views
"""
from django.contrib import admin
from .models import Item, List

class ItemInline(admin.TabularInline):
    """
    Inline configuration for Items.
    """
    model = Item
    extra = 1

class ListAdmin(admin.ModelAdmin):
    """
    Admin view: List with inlined Items.
    """
    list_display = ('name', 'description', 'image')
    search_fields = ('name',)
    list_filter = ('name',)
    inlines = [ItemInline]

admin.site.register(List, ListAdmin)

class ItemAdmin(admin.ModelAdmin):
    """
    Admin view: Item
    """
    list_display = ('name', 'amount', 'price', 'list')
    search_fields = ('name',)
    list_filter = ('amount',)

admin.site.register(Item, ItemAdmin)
