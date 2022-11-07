from rest_framework import serializers
from .models import api

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = api
        fields = ('id', 'title', 'description', 'completed')