from django.db import models
from datetime import datetime

# Create your models here.

class Contactadmin(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=130)
    email = models.CharField(max_length=130)
    service = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=5999)

def __str__(self):
    return self.email    