from django.db import models
from trip.models import Trip


class ScrapAndPayment(models.Model):
    photo = models.ImageField(upload_to='scrap_payment_photos/', blank=True)
    customer_received_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    scrap_partner_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE, related_name='scrap_payment')

    def __str__(self):
        return f"Scrap and Payment {self.id} - Trip: {self.trip.id}"
