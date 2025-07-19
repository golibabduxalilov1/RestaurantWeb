from django.contrib import admin
from .models import Chef, ContactInfo
from unfold.admin import ModelAdmin


@admin.register(Chef)
class ChefAdmin(ModelAdmin):

    list_display = ["name", "position", "experience_years", "is_featured"]
    list_filter = ["is_featured", "position"]
    search_fields = ["name", "position"]


@admin.register(ContactInfo)
class ContactInfoAdmin(ModelAdmin):

    list_display = ["email", "phone", "created_at"]
