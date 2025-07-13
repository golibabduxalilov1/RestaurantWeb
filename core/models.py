from django.db import models
from django.contrib.auth.models import User


class Chef(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    bio = models.TextField()
    image = models.ImageField(
        upload_to="chefs/", height_field=None, width_field=None, max_length=100
    )
    experience_years = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):

    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    opening_hours = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return f"Contact Info - {self.email}"
