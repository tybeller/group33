from django.contrib import admin

from .models import dogs
from .models import api

admin.site.register(dogs)

class ApiAdmin(admin.ModelAdmin):
    list_desplay = ("title", "description", "completed")

admin.site.register(api,ApiAdmin)