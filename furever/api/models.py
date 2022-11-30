from djongo import models
from django.forms import IntegerField
from django.contrib.postgres.fields import ArrayField

#TODO see if import from djongo works

#must install pillow for imageField

class dogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    breed = models.CharField(max_length=60, default='')
    sex = models.CharField(max_length=10, default='')
    weight = models.CharField(max_length=3, default='')
    age = models.CharField(max_length=10, default='')
    location = models.CharField(max_length=100, default='')
    attributes = models.TextField(default='{[]}')
    images = models.TextField(default='{[]}')
    desc = models.TextField(default='')

class api(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    