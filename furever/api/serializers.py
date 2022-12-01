from rest_framework import serializers
from .models import api
from .models import dogs
from .models import logins
from .models import profiles

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = api
        fields = ('id', 'title', 'description', 'completed')

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = dogs
        fields = ('name', 'breed', 'sex', 'weight', 'age', 'location', 'description', 'images', 'attributes')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = logins
        fields = ('username', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profiles
        fields = ('id', 'preferences')