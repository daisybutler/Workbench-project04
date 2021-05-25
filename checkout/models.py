import uuid

from django.db import models
from django.conf import settings

from plans.models import Plan


class Purchase(models.Model):
    
