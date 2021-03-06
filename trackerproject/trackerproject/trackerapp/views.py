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
        print(request.headers)
        logging.warning(request.headers)
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
