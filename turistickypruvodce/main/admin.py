from django.contrib import admin
from .models import Sight

class SightAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "location", "description"]

# Register your models here.
admin.site.register(Sight, SightAdmin)