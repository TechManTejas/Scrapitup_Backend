from rest_framework import viewsets
from customer.models import Customer, CustomerAddress
from customer.serializers import CustomerAddressSerializer, CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer
