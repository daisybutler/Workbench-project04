from django.db import models


class Locations(models.Model):
    location = models.CharField(max_length=30)
    lat = models.FloatField(max_length=10)
    lng = models.FloatField(max_length=10)

    def __str__(self):
        return self.location
