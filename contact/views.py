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
            return redirect("contact:contact")
    else:
        form = ContactForm()

    contact_info = ContactInfo.objects.first()
    google_map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2922.3268090152345!2d65.7851253!3d38.845298!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f4ea6219349c8fb%3A0x9879a3d21a724458!2sASI%20Park!5e0!3m2!1sen!2s!4v1720971023456!5m2!1sen!2s"

    context = {
        "form": form,
        "contact_info": contact_info,
        "google_map_url": google_map_url,
    }

    return render(req, "contact/contact.html", context)
