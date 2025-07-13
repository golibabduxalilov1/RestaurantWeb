from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from core.models import ContactInfo


def contact(req):
    if req.method == "POST":
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(
                req, "Thank you for your message! We will get back to you soon."
            )
    else:
        form = ContactForm()

    contact_info = ContactInfo.objects.first()

    context = {
        "form": form,
        "contact_info": contact_info,
    }

    return render(req, "contact/contact.html", context)
