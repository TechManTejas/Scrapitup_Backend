from rest_framework import serializers

from scrap.serializers import ScrapAndPaymentSerializer
from .models import Trip, TripStatusHistory


class TripStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TripStatusHistory
        fields = ['id', 'timestamp', 'status']


class TripSerializer(serializers.ModelSerializer):
    status_history = TripStatusHistorySerializer(many=True, read_only=True)
    scrap_payment = ScrapAndPaymentSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = ['id', 'customer', 'scrap_partner', 'notes', 'address', 'initiate_datetime',
                  'completion_datetime', 'current_status', 'rating', 'status_history']
