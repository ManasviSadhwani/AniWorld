from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Adoption(models.Model):

    animal_choices = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Horse', 'Horse'),
        ('Rabbit', 'Rabbit'),
        ('Fish', 'Fish'),
        ('Bird', 'Bird'),
        ('Rat', 'Rat'),
    )

    animal = models.CharField(choices=animal_choices, max_length=255)
    breed = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/adopt/%Y/%m/')
    description = RichTextField()
    age = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    

    