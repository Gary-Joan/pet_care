from django.contrib import admin
from .models import pet_appointment
from .models import Event
admin.site.register(pet_appointment)

admin.site.register(Event)