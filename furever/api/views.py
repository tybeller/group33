from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ApiSerializer
from .models import api

class ApiView(viewsets.ModelViewSet):
    #create serailizer class and assigne it to the ApiSerializer Class
    serializer_class = ApiSerializer
    
    #define a variable and populate it with api list obkect
    queryset = api.objects.all()

def helloWorld(request):
    return HttpResponse("Hello World")

