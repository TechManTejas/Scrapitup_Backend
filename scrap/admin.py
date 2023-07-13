from django.contrib import admin
from .models import ScrapAndPayment


@admin.register(ScrapAndPayment)
class ScrapAndPaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'trip', 'customer_received_amount', 'scrap_partner_amount']
