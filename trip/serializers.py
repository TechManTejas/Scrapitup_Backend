from rest_framework import serializers
from customer.models import Customer

from vendor.models import ScrapPartner
from .models import Trip, TripStatusHistory


class TripStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TripStatusHistory
        fields = ['id', 'timestamp', 'status']


class TripSerializer(serializers.ModelSerializer):
    status_history = TripStatusHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Trip
        fields = ['id', 'customer', 'scrap_partner', 'notes', 'address', 'initiate_datetime',
                  'completion_datetime', 'current_status', 'rating', 'scrap_photo', 'scrap_partner_amount', 'customer_received_amount', 'status_history']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        user_id = self.context.get('request').user.id

        is_customer = Customer.objects.filter(user_id=user_id).exists()
        is_scrap_partner = ScrapPartner.objects.filter(
            user_id=user_id).exists()

        if is_customer:
            exclude_fields = ['scrap_photo', 'scrap_partner_amount', 'status_history']
            for field in exclude_fields:
                representation.pop(field, None)
        elif is_scrap_partner:
            exclude_fields = ['customer', 'rating', 'customer_received_amount', 'status_history']
            for field in exclude_fields:
                representation.pop(field, None)

        return representation
