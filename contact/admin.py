from django.contrib import admin
from .models import ContactMessage
from unfold.admin import ModelAdmin


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):

    list_display = ["name", "email", "subject", "is_read", "created_at"]
    list_filter = ["is_read", "created_at"]
    search_fields = ["name", "email", "subject"]
    readonly_fields = ["created_at"]

    def mark_as_read(req, self, queryset):
        queryset.update(is_read=True)

    mark_as_read.short_description = "Mark selected messages as read"
    actions = ["mark_as_read"]
