from django.contrib import admin
from .models import Item, List

class ItemInline(admin.TabularInline):
    """
    Inline configuration for Items.
    """
    model = Item
    extra = 1  # Number of empty forms to display by default in the admin

class ListAdmin(admin.ModelAdmin):
    """
    Admin view: List with inlined Items.
    """
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    inlines = [ItemInline]  # Add this line to inline the Item model

admin.site.register(List, ListAdmin)

class ItemAdmin(admin.ModelAdmin):
    """
    Admin view: Item
    """
    list_display = ('name', 'amount', 'price', 'list')  # Add the 'list' field to the display
    search_fields = ('name',)
    list_filter = ('amount',)

admin.site.register(Item, ItemAdmin)
