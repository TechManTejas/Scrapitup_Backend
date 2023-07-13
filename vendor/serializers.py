from rest_framework import serializers

from trip.serializers import TripSerializer
from user.serializers import UserSerializer
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
    user = UserSerializer(read_only=True)
    address = ScrapPartnerAddressSerializer(many=True, read_only=True)
    rate_chart = serializers.SerializerMethodField()

    class Meta:
        model = ScrapPartner
        fields = ['id', 'user', 'photo', 'rating', 'address', 'rate_chart']

    def get_rate_chart(self, obj):
        rate_chart = ScrapPartnerRateChart.objects.filter(scrap_partner=obj)
        serializer = ScrapPartnerRateChartSerializer(rate_chart, many=True)
        return serializer.data


class ScrapPartnerSelfSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    address = ScrapPartnerAddressSerializer(many=True, read_only=True)
    rate_chart = serializers.SerializerMethodField()
    trips = TripSerializer(many=True, read_only=True)

    class Meta:
        model = ScrapPartner
        fields = ['id', 'user', 'photo', 'rating', 'address', 'rate_chart', 'trips']

    def get_rate_chart(self, obj):
        rate_chart = ScrapPartnerRateChart.objects.filter(scrap_partner=obj)
        serializer = ScrapPartnerRateChartSerializer(rate_chart, many=True)
        return serializer.data
