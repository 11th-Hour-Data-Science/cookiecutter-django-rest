from rest_framework import serializers
from .models import Stations, Measurements


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stations
        fields = "__all__"


class MeasurementSerializer(serializers.ModelSerializer):
    station = serializers.PrimaryKeyRelatedField(queryset=Stations.objects.all())

    class Meta:
        model = Measurements
        fields = "__all__"