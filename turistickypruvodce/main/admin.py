from django.contrib import admin
from .models import Sight
from .models import State
from .models import Categorie
from .models import SightCategorie

class SightAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "location", "description"]

class StateAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class CategorieAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class SightCategorieAdmin(admin.ModelAdmin):
    list_display = ["sight", "categorie"]

# Register your models here.
admin.site.register(Sight, SightAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(SightCategorie, SightCategorieAdmin)
