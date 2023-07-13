from rest_framework import viewsets
from .models import ScrapPartner, ScrapPartnerAddress, ScrapPartnerRateChart
from .serializers import ScrapPartnerSerializer, ScrapPartnerAddressSerializer, ScrapPartnerRateChartSerializer


class ScrapPartnerViewSet(viewsets.ModelViewSet):
    queryset = ScrapPartner.objects.all()
    serializer_class = ScrapPartnerSerializer


class ScrapPartnerAddressViewSet(viewsets.ModelViewSet):
    queryset = ScrapPartnerAddress.objects.all()
    serializer_class = ScrapPartnerAddressSerializer


class ScrapPartnerRateChartViewSet(viewsets.ModelViewSet):
    queryset = ScrapPartnerRateChart.objects.all()
    serializer_class = ScrapPartnerRateChartSerializer
