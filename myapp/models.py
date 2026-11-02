from django.db import models
from django.contrib.auth.models import User

user = models.ForeignKey(User, on_delete=models.CASCADE)

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Soil(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Crop(models.Model):
    crop_name = models.CharField(max_length=50)
    seed = models.CharField(max_length=50)
    soil = models.ForeignKey(Soil, on_delete=models.CASCADE)
    soil_ph = models.FloatField()
    climate = models.CharField(max_length=50)
    temperature = models.IntegerField()
    rainfall = models.IntegerField()
    water_ph = models.FloatField()
    fertilizer = models.CharField(max_length=50)
    harvest_days = models.IntegerField()
    yield_ton = models.FloatField()


    def __str__(self):
        return self.crop_name
