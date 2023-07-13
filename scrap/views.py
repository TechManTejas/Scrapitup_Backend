from rest_framework import viewsets
from .models import ScrapAndPayment
from .serializers import ScrapAndPaymentSerializer


class ScrapAndPaymentViewSet(viewsets.ModelViewSet):
    queryset = ScrapAndPayment.objects.all()
    serializer_class = ScrapAndPaymentSerializer
