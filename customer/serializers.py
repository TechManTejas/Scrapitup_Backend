from rest_framework import serializers
from customer.models import Customer, CustomerAddress
from trip.serializers import TripSerializer
from user.serializers import UserSerializer


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'


class CustomerGetSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    addresses = CustomerAddressSerializer(many=True, read_only=True)
    trips = TripSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone_number', 'addresses', 'trips']


class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['phone_number']
