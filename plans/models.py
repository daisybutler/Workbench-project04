from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_id = models.CharField(max_length=200)
    plan_type = models.CharField(max_length=25)
    short_description = models.TextField()
    long_description = models.TextField()
    hours_incl = models.TextField()
    access_times = models.TextField()
    wifi = models.BooleanField(default=True)
    disabled_access = models.BooleanField(default=True)
    extra_info = models.TextField()

    def __str__(self):
        return self.name
