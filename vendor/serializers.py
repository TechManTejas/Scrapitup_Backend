from rest_framework import serializers

from trip.serializers import TripSerializer
from .models import ScrapPartner, ScrapPartnerAddress, ScrapPartnerRateChart


class ScrapPartnerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapPartnerAddress
        fields = '__all__'


class ScrapPartnerRateChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapPartnerRateChart
        fields = ['id', 'scrap_partner', 'item', 'rate']


class ScrapPartnerSerializer(serializers.ModelSerializer):
    address = ScrapPartnerAddressSerializer()
    trips = TripSerializer(many=True, read_only=True)
    rate_chart = serializers.SerializerMethodField()

    class Meta:
        model = ScrapPartner
        fields = ['id', 'user', 'phone_number', 'photo', 'id_proof', 'rating', 'address', 'trips']

    def get_rate_chart(self, obj):
        rate_chart = ScrapPartnerRateChart.objects.filter(scrap_partner=obj)
        serializer = ScrapPartnerRateChartSerializer(rate_chart, many=True)
        return serializer.data

