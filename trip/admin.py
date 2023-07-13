from django.contrib import admin
from .models import Trip, TripStatusHistory


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['customer', 'scrap_partner', 'initiate_datetime', 'completion_datetime', 'current_status']


@admin.register(TripStatusHistory)
class TripStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ['trip', 'timestamp', 'status']
    # Add more fields as needed
