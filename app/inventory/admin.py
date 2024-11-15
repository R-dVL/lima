from django.contrib import admin
from .models import Article, List

class ArticleInline(admin.TabularInline):
    """
    Inline configuration for Articles.
    """
    model = Article
    extra = 1  # Number of empty forms to display by default in the admin

class ListAdmin(admin.ModelAdmin):
    """
    Admin view: List with inlined Articles.
    """
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    inlines = [ArticleInline]  # Add this line to inline the Article model

admin.site.register(List, ListAdmin)

class ArticleAdmin(admin.ModelAdmin):
    """
    Admin view: Article
    """
    list_display = ('name', 'quantity', 'price', 'list')  # Add the 'list' field to the display
    search_fields = ('name',)
    list_filter = ('quantity',)

admin.site.register(Article, ArticleAdmin)
