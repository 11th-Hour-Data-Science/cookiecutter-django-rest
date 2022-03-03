from rest_framework import viewsets, mixins

from .models import Stations, Measurements
from .serializers import StationSerializer, MeasurementSerializer


class StationViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Stations.objects.all()
    serializer_class = StationSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    """
    Creates user accounts
    """
    queryset = Measurements.objects.all()
    serializer_class = MeasurementSerializer

