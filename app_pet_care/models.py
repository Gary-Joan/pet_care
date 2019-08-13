
from django.db import models
from django.urls import reverse

class pet_appointment(models.Model):
    pet_name = models.CharField(max_length=200)
    date = models.DateField()
    hour = models.TimeField()

    def __str__(self):
        return self.pet_name

    def __unicode__(self):
        return self.date

    def __unicode__(self):
        return self.hour



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()


    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
