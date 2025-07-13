from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ["first_name", "last_name", "guest_count", "date", "time", "status"]
    list_filter = ["status", "date", "guest_count"]

    search_fields = ["first_name", "last_name", "email"]
    actions = ["approve_reservations", "reject_reservations"]

    def approve_reservations(self, req, queryset):
        for reservation in queryset:
            reservation.status = "approved"
            reservation.save()
            reservation.send_confirmation_email()
        self.message_user(
            req, f"{queryset.count()} reservations approved and emails sent."
        )

    def reject_reservations(self, req, queryset):
        for reservation in queryset:
            reservation.status = "rejected"
            reservation.save()
            reservation.send_confirmation_email()
        self.message_user(
            req, f"{queryset.count()} reservations rejected and emails sent."
        )

    approve_reservations.short_description = "Approve selected reservations"
    reject_reservations.short_description = "Reject selected reservations"
