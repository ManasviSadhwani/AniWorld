from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Vets(models.Model):

    name = models.CharField(max_length=2055)
    number = models.CharField(max_length=2055)
    clinic = models.CharField(max_length=2955)
    photo = models.ImageField(upload_to='media/adopt/%Y/%m/')
    description = RichTextField()
    degree = models.CharField(max_length=555)
    fee = models.IntegerField()
    time = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    


    