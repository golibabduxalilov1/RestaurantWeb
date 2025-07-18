from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Chef, ContactInfo
from menu.models import MenuItem
from blog.models import BlogPost
from reservations.forms import ReservationForm
from menu.models import Category, MenuItem


def home(req):
    featured_chefs = Chef.objects.filter(is_featured=True)[:4]
    featured_items = MenuItem.objects.filter(is_featured=True)[:6]
    latest_posts = BlogPost.objects.filter(is_published=True)[:3]
    google_map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2922.3268090152345!2d65.7851253!3d38.845298!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f4ea6219349c8fb%3A0x9879a3d21a724458!2sASI%20Park!5e0!3m2!1sen!2s!4v1720971023456!5m2!1sen!2s"
    categories = (
        Category.objects.filter(is_activate=True)
        .prefetch_related("menuitem_set")
        .order_by("order", "name")
    )
    if req.method == "POST":
        form = ReservationForm(req.POST)
        if form.is_valid():
            reservation = form.save()
            messages.success(
                req,
                "Your reservation has been submitted successfully! We will contact you soon.",
            )
            return redirect("reservation:make_reservation")

    else:
        form = ReservationForm()

    context = {
        "featured_chefs": featured_chefs,
        "featured_items": featured_items,
        "latest_posts": latest_posts,
        "google_map_url": google_map_url,
        "form": form,
        "categories": categories,
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
