from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloWorld, name='Hello World')
]