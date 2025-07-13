from django.shortcuts import render
from .models import Category, MenuItem


def menu(req):
    categories = Category.objects.filter(is_active=True).prefetch_related(
        "menuitem_set"
    )

    context = {"categories": categories}

    return render(req, "menu/menu.html")
