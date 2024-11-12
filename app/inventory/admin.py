"""
Admin configuration for the 'inventory' app.
"""
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    """
    Admin view: Article
    """
    list_display = ('name', 'quantity', 'price')
    search_fields = ('name',)
    list_filter = ('quantity',)

admin.site.register(Article, ArticleAdmin)
