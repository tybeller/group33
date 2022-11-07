from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

#create router object
router = routers.DefaultRouter()
#register the router
router.register('tasks', views.ApiView, 'task')

urlpattern = [
    path('admin/', admin.site.urls),
    
    #add another path to url patterns
    #when visiting localhost:8000/api
    #should be routed to django rest framework
    
    path('api/', include(router.urls))
]