from django.contrib import admin
from .models import Chef, ContactInfo


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):

    list_display = ["name", "position", "experience_years", "is_featured"]
    list_filter = ["is_featured", "position"]
    search_fields = ["name", "position"]


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):

    list_display = ["email", "phone", "created_at"]
