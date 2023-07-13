from rest_framework import viewsets
from .models import Trip, TripStatusHistory
from .serializers import TripSerializer, TripStatusHistorySerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripStatusHistoryViewSet(viewsets.ModelViewSet):
    queryset = TripStatusHistory.objects.all()
    serializer_class = TripStatusHistorySerializer
