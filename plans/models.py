from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    features = models.TextField()

    def __str__(self):
        return self.name
