from django.db import models
from datetime import datetime

from django.db.models.fields import EmailField
from ckeditor.fields import RichTextField


# Create your models here.

class Ngo(models.Model):

    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    mission = models.CharField(max_length=5000)
    photo = models.ImageField(upload_to='media/ngo/%Y/%m/')
    description = RichTextField()
    city = models.CharField(max_length=255)
    email = models.EmailField(default="")
    established = models.IntegerField()
    awards = models.IntegerField()
    total_animals = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
