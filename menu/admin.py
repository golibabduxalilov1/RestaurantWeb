from django.contrib import admin
from .models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ["name", "order", "is_activate"]
    list_filter = ["order", "is_activate"]
    ordering = ["order"]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ["name", "category", "price", "is_featured", "is_available"]
    list_filter = ["category", "is_featured", "is_available"]
    search_fields = ["name", "description"]
    list_editable = ["is_featured", "is_available"]
