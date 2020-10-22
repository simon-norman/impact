from django.db import models

class Journey(models.Model):

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    carbon_journey_id = models.ForeignKey(Journey, on_delete=models.CASCADE)
