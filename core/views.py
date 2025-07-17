from django.shortcuts import render
from .models import Chef, ContactInfo
from menu.models import MenuItem
from blog.models import BlogPost


def home(request):
    featured_chefs = Chef.objects.filter(is_featured=True)[:4]
    featured_items = MenuItem.objects.filter(is_featured=True)[:6]
    latest_posts = BlogPost.objects.filter(is_published=True)[:3]
    google_map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2922.3268090152345!2d65.7851253!3d38.845298!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f4ea6219349c8fb%3A0x9879a3d21a724458!2sASI%20Park!5e0!3m2!1sen!2s!4v1720971023456!5m2!1sen!2s"

    context = {
        "featured_chefs": featured_chefs,
        "featured_items": featured_items,
        "latest_posts": latest_posts,
        "google_map_url": google_map_url,
    }
    return render(request, "core/home.html", context)


def about(request):
    chefs = Chef.objects.all()
    contact_info = ContactInfo.objects.first()

    context = {
        "chefs": chefs,
        "contact_info": contact_info,
    }
    return render(request, "core/about.html", context)
