from datetime import datetime
from django.db.models import Q
from rest_framework import viewsets
from .models import Trip, TripStatusHistory
from rest_framework.response import Response
from .serializers import TripSerializer, TripStatusHistorySerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.filter(Q(customer__user_id=self.request.user.id) | Q(scrap_partner__user_id=self.request.user.id))

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if 'current_status' in serializer.validated_data and serializer.validated_data['current_status'] == 'Completed':
            serializer.validated_data['completion_datetime'] = datetime.now()

        self.perform_update(serializer)

        return Response(serializer.data)

class RequestedTripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.filter((Q(customer__user_id=self.request.user.id) | Q(scrap_partner__user_id=self.request.user.id)) & Q(current_status="Request Generated"))


class AcceptedTripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.filter((Q(customer__user_id=self.request.user.id) | Q(scrap_partner__user_id=self.request.user.id)) & Q(current_status="Request Accepted"))


class ArrivingTripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.filter((Q(customer__user_id=self.request.user.id) | Q(scrap_partner__user_id=self.request.user.id)) & Q(current_status="Arriving Today"))


class VerifiedTripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.filter((Q(customer__user_id=self.request.user.id) | Q(scrap_partner__user_id=self.request.user.id)) & Q(current_status="Arrivied & Verified"))


class CompletedTripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.filter((Q(customer__user_id=self.request.user.id) | Q(scrap_partner__user_id=self.request.user.id)) & Q(current_status="Completed"))


class RejectedTripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.filter((Q(customer__user_id=self.request.user.id) | Q(scrap_partner__user_id=self.request.user.id)) & Q(current_status="Rejected"))


class CancelledTripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.filter((Q(customer__user_id=self.request.user.id) | Q(scrap_partner__user_id=self.request.user.id)) & Q(current_status="Cancelled"))


class TripStatusHistoryViewSet(viewsets.ModelViewSet):
    queryset = TripStatusHistory.objects.all()
    serializer_class = TripStatusHistorySerializer
