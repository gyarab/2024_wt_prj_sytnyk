from django.contrib import admin
from .models import Sight
from .models import State
from .models import Categorie

class SightAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "location", "description"]

class StateAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class CategorieAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

# Register your models here.
admin.site.register(Sight, SightAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Categorie, CategorieAdmin)