from djongo import models
from django.forms import IntegerField

#TODO see if import from djongo works

#must install pillow for imageField

class dogs(models.Model):
    name = models.CharField(max_length=60)
    breed = models.CharField(max_length=60)
    age = models.PositiveIntegerField()
    desc = models.TextField()
    
