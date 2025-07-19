from django import forms
from .models import Reservation
from datetime import time


class ReservationForm(forms.ModelForm):
    TIME_CHOICES = [
        (time(13, 0), "1:00 PM"),
        (time(13, 30), "1:30 PM"),
        (time(14, 0), "2:00 PM"),
        (time(14, 30), "2:30 PM"),
        (time(15, 0), "3:00 PM"),
        (time(15, 30), "3:30 PM"),
        (time(16, 0), "4:00 PM"),
        (time(16, 30), "4:30 PM"),
        (time(17, 0), "5:00 PM"),
        (time(17, 30), "5:30 PM"),
        (time(18, 0), "6:00 PM"),
        (time(18, 30), "6:30 PM"),
        (time(19, 0), "7:00 PM"),
        (time(19, 30), "7:30 PM"),
        (time(20, 0), "8:00 PM"),
        (time(20, 30), "8:30 PM"),
        (time(21, 0), "9:00 PM"),
    ]

    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500 p-2 border",
                "required": True,
            }
        ),
    )

    class Meta:
        model = Reservation
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "guest_count",
            "date",
            "time",
            "special_requests",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500 p-2 border",
                    "required": True,
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500 p-2 border",
                    "required": True,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500 p-2 border",
                    "required": True,
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500 p-2 border",
                    "type": "tel",
                    "required": True,
                }
            ),
            "guest_count": forms.Select(
                attrs={
                    "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500 p-2 border",
                    "required": True,
                }
            ),
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500 p-2 border",
                    "required": True,
                }
            ),
            "special_requests": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500 p-2 border",
                }
            ),
        }
