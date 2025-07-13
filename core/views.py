from django.shortcuts import render
from .models import Chef, ContactInfo
from menu.models import MenuItem
from blog.models import BlogPost


def home(req):
    featured_chefs = Chef.objects.filter(is_featured=True)[:3]
    featured_items = MenuItem.objects.filter(is_featured=True)[:6]
    latest_posts = BlogPost.objects.filter(is_featured=True)[:3]

    context = {
        "featured_chefs": featured_chefs,
        "featured_items": featured_items,
        "latest_posts": latest_posts,
    }

    return render(req, "core/home.html", context)


def about(req):
    chefs = Chef.objects.all()
    contact_info = ContactInfo.objects.first()

    context = {
        "chefs": chefs,
        "contact_info": contact_info,
    }

    return render(req, "core/about.html", context)
