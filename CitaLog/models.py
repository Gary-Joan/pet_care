# Create your models here.
from django.db import models
from django.urls import reverse

class EventCita(models.Model):
    doctor_name = models.CharField(max_length=25)
    pet_owner = models.CharField(max_length=25)
    title = models.CharField(max_length=200)
    race = models.CharField(max_length=25)
    description = models.TextField()
    pet_sym = models.TextField()
    prescription = models.TextField()
    start_time = models.DateField()
    date_start_time = models.TimeField()
    date_end_time = models.TimeField()

    @property
    def get_html_url(self):
        url = reverse('cita:event_editC', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class Services(models.Model):
    service_name = models.CharField(max_length=25)
    description = models.CharField(max_length=25)
    doctor_who_doit = models.CharField(max_length=200)
    price = models.IntegerField(default=0)