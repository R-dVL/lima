"""
Admin configuration for the 'inventory' app.
"""
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity_at_home', 'quantity_to_buy', 'price')
    search_fields = ('name',)
    list_filter = ('quantity_at_home',)

admin.site.register(Article, ArticleAdmin)