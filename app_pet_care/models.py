
from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()


    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class Veterinarian(models.Model):
    dpi = models.IntegerField()
    name = models.CharField(max_length=200)
    photo = models.FileField(upload_to='media/image_veterinarian', blank=True, null=True)
    telephone = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    birth_date = models.DateField()
    collected_number = models.IntegerField()
    password = models.CharField(max_length=50)
