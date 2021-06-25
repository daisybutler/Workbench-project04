import uuid
from django.db import models
from django.conf import settings


class Order(models.Model):
    order_id = models.CharField(max_length=32, null=False, editable=False)
    plan_name = models.CharField(max_length=200)
    plan_type = models.CharField(max_length=25)
    plan_friendly_name = models.CharField(max_length=200)
    qty = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, null=False, blank=False)
    password = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    billing_address = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def _generate_order_id(self):
        """
        Generate a random, unique order ID using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order ID
        if it hasn't been set already.
        """
        if not self.order_id:
            self.order_id = self._generate_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id
