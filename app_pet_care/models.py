from django.db import models

# Create your models here.

class pet_appointment(models.Model):
    pet_name = models.CharField(max_length=200)
    date = models.DateField()
    hour = models.DateTimeField()
"""
class species(model.Model):
    name_species = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    
class pet(model.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    species_pet = models.IntegerField()
"""