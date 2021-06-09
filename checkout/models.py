from django.db import models


class Order(models.Model):
    order_id = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200)
    qty = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    plan_type = models.CharField(max_length=25)
    short_description = models.TextField()
    long_description = models.TextField()

    def __str__(self):
        return self.order_id + self.name
