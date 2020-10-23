from django.db import models

class Journey(models.Model):

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    carbon_journey_id = models.ForeignKey(Journey, on_delete=models.CASCADE, blank=True)
    timestamp = models.DateTimeField()
    confirmed_no_journey = models.BooleanField(default=False) 
