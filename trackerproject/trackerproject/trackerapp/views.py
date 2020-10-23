from django.shortcuts import render
from .models import Location
from .serializers import LocationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

class HealthCheck(APIView):
    def get(self, request):
        return Response('Successful')
        
class LocationList(APIView):
    def post(self, request, format=None):
        location = request.data
        location['timestamp'] = datetime.datetime.fromtimestamp(location['timestamp'])
        serializer = LocationSerializer(data=location)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
