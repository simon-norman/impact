from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.Serializer):
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)

    def create(self, validated_data):
        return Location.objects.create(**validated_data)