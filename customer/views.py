from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from customer.models import Customer, CustomerAddress
from rest_framework.permissions import AllowAny, IsAuthenticated
from customer.serializers import CustomerAddressSerializer, CustomerGetSerializer, CustomerCreateSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerGetSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomerCreateSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user.id)

    def create(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')

        user, user_created = User.objects.get_or_create(username=phone_number, password=phone_number)

        if user_created:
            Customer.objects.get_or_create(
                user=user, phone_number=phone_number)
        else:
            Customer.objects.get(user__username=user)

        token, token_created = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
        })


class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer
