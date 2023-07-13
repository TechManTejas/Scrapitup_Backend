from django.contrib import admin
from .models import ScrapPartner, ScrapPartnerAddress, ScrapPartnerRateChart


@admin.register(ScrapPartner)
class ScrapPartnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']


@admin.register(ScrapPartnerAddress)
class ScrapPartnerAddressAdmin(admin.ModelAdmin):
    list_display = ['scrap_partner', 'state', 'district', 'pincode']


@admin.register(ScrapPartnerRateChart)
class ScrapPartnerRateChartAdmin(admin.ModelAdmin):
    list_display = ['id', 'scrap_partner', 'item', 'rate']