from django.forms import ModelForm, DateInput, TimeInput
from .models import EventCita, Services
from django import forms
from .models import EventCita, Utensilio

class EventForm(ModelForm):
  class Meta:
    model = EventCita
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
        'start_time': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        'date_start_time': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        'date_end_time': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field

    self.fields['start_time'].input_formats = ('%Y-%m-%d',)

    self.fields['date_start_time'].input_formats = ('%H:%M',)
    self.fields['date_end_time'].input_formats = ('%H:%M',)

    self.fields['doctor_name'].label = "Doctor que atiende"
    self.fields['title'].label = "Nombre Mascota"
    self.fields['pet_owner'].label = "Dueño de la mascota"
    self.fields['race'].label = "Raza de la mascota"
    self.fields['pet_sym'].label = "Simtomas descritos"
    self.fields['prescription'].label = "Preescripciones"
    self.fields['start_time'].label = "FECHA DE LA CITA"
    self.fields['date_start_time'].label = "HORA INICIO CITA"
    self.fields['date_end_time'].label = "HORA FIN CITA"

class ServiceForm(forms.ModelForm):
  class Meta:
    model = Services


    fields = [
      'service_name',
      'description',
      'doctor_who_doit',
      'price'
    ]

    labels = {
      'service_name': 'Nombre del Servicio',
      'description': 'Description del servicio',
      'doctor_who_doit': 'Doctor A Cargo',
      'price': 'Precio Servicio',
    }

    widgets ={
      'description': forms.Textarea(attrs={'required':False}),

    }
class UtensilioForm(ModelForm):
  class Meta:
    model = Utensilio
    fields = ['id', 'nombre', 'descripcion']