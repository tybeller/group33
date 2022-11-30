from rest_framework import serializers
from .models import api
from .models import dogs

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = api
        fields = ('id', 'title', 'description', 'completed')

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = dogs
        #fields = ('id', 'name', 'breed', 'sex', 'weight', 'age', 'location', 'desc') # 'attributes', 'images'
        fields = ('name', 'breed', 'sex', 'age')