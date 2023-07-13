from rest_framework import serializers
from .models import ScrapAndPayment


class ScrapAndPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapAndPayment
        fields = ['id', 'photo', 'customer_received_amount','scrap_partner_amount', 'trip']
