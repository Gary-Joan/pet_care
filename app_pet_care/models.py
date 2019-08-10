
from django.db import models


class pet_appointment(models.Model):
    pet_name = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()
    hour = models.TimeField()

    def __str__(self):
        return self.pet_name

    def __unicode__(self):
        return self.date

    def __unicode__(self):
        return self.hour
