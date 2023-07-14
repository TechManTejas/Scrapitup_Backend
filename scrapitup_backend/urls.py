from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from user.views import UserModelViewSet
from customer.views import CustomerViewSet, CustomerAddressViewSet
from vendor.views import ScrapPartnerViewSet, ScrapPartnerAddressViewSet
from trip.views import AcceptedTripViewSet, ArrivingTripViewSet, CancelledTripViewSet, CompletedTripViewSet, RejectedTripViewSet, RequestedTripViewSet, TripViewSet, TripStatusHistoryViewSet, VerifiedTripViewSet
from rates.views import ItemViewSet
from vendor.views import ScrapPartnerRateChartViewSet

router = DefaultRouter()
router.register('user', UserModelViewSet, basename='user')

router.register('customer', CustomerViewSet, basename='customer')
router.register('customer-address', CustomerAddressViewSet, basename='customer-address')

router.register('scrap-partner', ScrapPartnerViewSet, basename='scrap-partner')
router.register('scrap-partner-address',ScrapPartnerAddressViewSet, basename='scrap-partner-address')
router.register('scrap-partner-rate-chart',ScrapPartnerRateChartViewSet, basename='scrap-partner-rate-chart')

router.register('trip', TripViewSet, basename='trip')
router.register('requested-trip', RequestedTripViewSet,basename='requested-trip')
router.register('requested-trip', AcceptedTripViewSet,basename='requested-trip')
router.register('requested-trip', ArrivingTripViewSet,basename='requested-trip')
router.register('requested-trip', VerifiedTripViewSet,basename='requested-trip')
router.register('requested-trip', CompletedTripViewSet,basename='requested-trip')
router.register('requested-trip', RejectedTripViewSet,basename='requested-trip')
router.register('requested-trip', CancelledTripViewSet,basename='requested-trip')

router.register('trip-status-history', TripStatusHistoryViewSet,basename='trip-status-history')
router.register('item', ItemViewSet, basename='item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
