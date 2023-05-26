from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Item(TimeStampedModel, models.Model):
    name = models.CharField(max_length=50)