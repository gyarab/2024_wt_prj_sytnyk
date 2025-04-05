from django.db import models

class Sight(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    description = models.TextField(blank=True, default="")
    link = models.CharField(max_length=300, blank=True, default="")
    #director = models.ForeignKey("Director", on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey("State", on_delete=models.SET_NULL, null=True)
    categorie = models.ForeignKey("Categorie", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Sight <{self.id}> {self.name} ({self.location})"

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"State <{self.id}> {self.name}"

class Categorie(models.Model):
    name = models.CharField(max_length=50)
    sight = models.ForeignKey("Sight", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Categorie <{self.id}> {self.name}"
