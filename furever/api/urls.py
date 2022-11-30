#from django.contrib import admin
#from django.urls import path, include
from api import views
#from rest_framework import routers

#create router object
#router = routers.DefaultRouter()
#register the router
#router.register('tasks', views.ApiView, 'task')

#urlpattern = [
#    path('admin/', admin.site.urls),
    
    #add another path to url patterns
    #when visiting localhost:8000/api
    #should be routed to django rest framework
    
#    path('api/', include(router.urls))
#]


from django.conf.urls import url
from tutorials import views

urlpatterns = [ 
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published)
]