from django.db import models

class Sight(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    description = models.TextField(blank=True, default="")
    link = models.CharField(max_length=300, blank=True, default="")
    #director = models.ForeignKey("Director", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Movie <{self.id}> {self.name} ({self.location})"

class State(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=50)
