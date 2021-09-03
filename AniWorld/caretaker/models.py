from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.

class Caretaker(models.Model):

    animal_choices = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Horse', 'Horse'),
        ('Rabbit', 'Rabbit'),
        ('Fish', 'Fish'),
        ('Bird', 'Bird'),
        ('Rat', 'Rat'),
    )


    name = models.CharField(max_length=255)
    price = models.IntegerField()
    number = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/caret/%Y/%m/')
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    max_days = models.IntegerField()
    preferred_animal = models.CharField(choices=animal_choices ,max_length=255)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
