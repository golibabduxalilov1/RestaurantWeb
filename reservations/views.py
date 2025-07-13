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
            return redirect("reservations:make_reservation")

    else:
        form = ReservationForm()

    return render(req, "reservations/make_reservation", {"form": form})
