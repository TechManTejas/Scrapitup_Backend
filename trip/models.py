from django.db import models
from customer.models import Customer, CustomerAddress
from vendor.models import ScrapPartner


class Trip(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='trips')
    scrap_partner = models.ForeignKey(ScrapPartner, on_delete=models.CASCADE, related_name='trips')
    notes = models.TextField(blank=True)
    address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE)
    initiate_datetime = models.DateTimeField(auto_now_add=True)
    completion_datetime = models.DateTimeField(blank=True, null=True)
    current_status = models.CharField(max_length=100, default="Request Generated")
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Trip {self.id} - Customer: {self.customer.user.username} - Scrap Partner: {self.scrap_partner.user.username}"


class TripStatusHistory(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='status_history')
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Trip: {self.trip.id} - Timestamp: {self.timestamp} - Status: {self.status}"
