from rest_framework import viewsets
from .models import ScrapPartner, ScrapPartnerAddress, ScrapPartnerRateChart
from .serializers import ScrapPartnerSelfSerializer, ScrapPartnerSerializer, ScrapPartnerAddressSerializer, ScrapPartnerRateChartSerializer


class ScrapPartnerViewSet(viewsets.ModelViewSet):
    queryset = ScrapPartner.objects.all()
    serializer_class = ScrapPartnerSerializer

    def get_serializer_class(self):
        scrap_partner = ScrapPartner.objects.filter(user=self.request.user.id)
        if scrap_partner:
            return ScrapPartnerSelfSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        scrap_partner = ScrapPartner.objects.filter(user=self.request.user.id)
        if scrap_partner:
            return scrap_partner
        else:
            return ScrapPartner.objects.all()


class ScrapPartnerAddressViewSet(viewsets.ModelViewSet):
    queryset = ScrapPartnerAddress.objects.all()
    serializer_class = ScrapPartnerAddressSerializer

    def get_queryset(self):
        return ScrapPartnerAddress.objects.filter(user=self.request.user.id)


class ScrapPartnerRateChartViewSet(viewsets.ModelViewSet):
    queryset = ScrapPartnerRateChart.objects.all()
    serializer_class = ScrapPartnerRateChartSerializer

    def get_queryset(self):
        return ScrapPartnerRateChart.objects.filter(user=self.request.user.id)
