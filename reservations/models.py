from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class Reservation(models.Model):
    GUEST_COUNT_CHOICES = [
        (1, "1 Person"),
        (2, "2 People"),
        (3, "3 People"),
        (4, "4+ People"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    guest_count = models.IntegerField(choices=GUEST_COUNT_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    special_requests = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date} {self.time}"

    def send_confirmation_email(self):
        subject = f"Reservation Confirmation - {self.get_status_display()}"

        if self.status == "approved":
            massage = f"""
            Dear {self.first_name},

            Your reservation has been approved!

            Details:
            - Date: {self.date}
            - Time: {self.time}
            - Guests: {self.get_guest_count_display()}
            - Special Requests: {self.special_requests}

            We look forward to seeing you!

            Best regards,
            Restaurant Team
            """
        else:
            massage = f"""
            Dear {self.first_name},

            Unfortunately, your reservation for {self.date} at {self.time} could not be confirmed.

            Please contact us to discuss alternative options.

            Best regards,
            Restaurant Team
            """

        send_mail(
            subject,
            massage,
            settings.DEFAULT_FROM_EMAIL,
            [self.email],
            fail_silently=False,
        )
