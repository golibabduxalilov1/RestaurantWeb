from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservationForm


def make_reservation(req):
    if req.method == "POST":
        form = ReservationForm(req.POST)
        if form.is_valid():
            reservation = form.save()
            messages.success(
                req,
                "Your reservation has been submitted successfully! We will contact you soon.",
            )
            return redirect("core:home")

    else:
        form = ReservationForm()
    google_map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2922.3268090152345!2d65.7851253!3d38.845298!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f4ea6219349c8fb%3A0x9879a3d21a724458!2sASI%20Park!5e0!3m2!1sen!2s!4v1720971023456!5m2!1sen!2s"

    context = {
        "form": form,
        "google_map_url": google_map_url,
    }

    return render(req, "reservation/make_reservation.html", context)
