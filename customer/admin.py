from django.contrib import admin
from customer.models import Customer, CustomerAddress


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']


@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'state', 'district', 'pincode']