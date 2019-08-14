from django import forms
from .models import pet_appointment
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput

class post_form_medical_appointment(forms.Form):
    form_name = forms.CharField(label='Nombre de mascota',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'mascota', 'required': True}))
    form_date = forms.DateField(label='Fecha', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}))
    form_hour = forms.TimeField(label='Hora', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'time', 'required': True}))

    class Meta:
        model = pet_appointment
        fields = ('form_name', 'form_date', 'form_hour')




from django.forms import ModelForm, DateInput
from .models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event

    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),

    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)

    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['title'].label = "Mascota"
    self.fields['description'].label = "Descripcion Del Problema"
    self.fields['doctor'].label = "Doctor que atiende"
    self.fields['pet_owner'].label = "Dueño de la mascota"
    self.fields['race'].label = "Raza de la mascota"
    self.fields['pet_sym'].label = "Simtomas descritos"
    self.fields['prescription'].label = "Preescripciones"
    self.fields['start_time'].label = "FECHA DE LA CITA"
    self.fields['date_start_time'].label = "HORA INICIO CITA"
    self.fields['date_end_time'].label = "HORA FIN CITA"

