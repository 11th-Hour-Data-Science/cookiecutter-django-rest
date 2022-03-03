from rest_framework import viewsets, mixins

from .models import Stations, Measurements
from .serializers import StationSerializer, MeasurementSerializer


class StationViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Stations.objects.all()
    serializer_class = StationSerializer


class MeasurementViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = Measurements.objects.all()
    serializer_class = MeasurementSerializer

