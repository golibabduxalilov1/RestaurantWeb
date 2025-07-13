from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = ["title", "author", "is_published", "created_at"]
    list_filter = ["is_published", "author", "created_at"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

    def save(self, req, obj, form, change):
        if not obj.author_id:
            obj.author = req.user
        super().save(self, req, obj, form, change)
