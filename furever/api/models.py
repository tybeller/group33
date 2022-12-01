from djongo import models
from django.forms import IntegerField
from django.contrib.postgres.fields import ArrayField

#TODO see if import from djongo works

#must install pillow for imageField

class dogs(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(default='')
    breed = models.TextField(default='')
    sex = models.TextField(default='')
    weight = models.TextField(default='')
    age = models.TextField(default='')
    location = models.TextField(default='')
    attributes = models.TextField(default='[]') # string representation of json array
    images = models.TextField(default='[]') # string representation of json array
    description = models.TextField(default='')

class logins(models.Model):
    username = models.TextField()
    password = models.TextField()

class profiles(models.Model):
    id = models.TextField(primary_key=True) # foreign key references logins
    username = models.TextField()
    preferences = models.TextField(default='[]') # string representation of json array

class api(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    