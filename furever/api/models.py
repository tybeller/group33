from djongo import models
from django.forms import IntegerField

#TODO see if import from djongo works

#must install pillow for imageField

class dogs(models.Model):
    name = models.CharField(max_length=60)
    breed = models.CharField(max_length=60)
    age = models.PositiveIntegerField()
    desc = models.TextField()

class api(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    
