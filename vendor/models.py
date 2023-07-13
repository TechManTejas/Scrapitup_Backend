from django.db import models
from django.contrib.auth.models import User

from rates.models import Item


class ScrapPartner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='scrap_partner_photos/')
    id_proof = models.ImageField(upload_to='scrap_partner_id_proofs/')
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.user.username


class ScrapPartnerAddress(models.Model):
    scrap_partner = models.ForeignKey(ScrapPartner, on_delete=models.CASCADE, related_name='address')
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    landmark = models.CharField(max_length=200)
    street_flat_no = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.scrap_partner.user.username}'s Address"


class ScrapPartnerRateChart(models.Model):
    scrap_partner = models.OneToOneField(ScrapPartner, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"Scrap Partner: {self.scrap_partner.user.username} - Item: {self.item.name} - Rate: {self.rate}"
