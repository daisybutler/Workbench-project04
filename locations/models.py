from django.db import models

# Create your models here.

class Locations(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location