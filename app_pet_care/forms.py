from django import forms
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.forms import ModelForm, DateInput
from .models import Event, Veterinarian

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
    self.fields['start_time'].label = "HORA DE LA CITA"

class login_veterinarian(forms.Form):
  user = forms.EmailField(label='Usuario', widget=forms.TextInput(attrs={'placeholder':'corre@correo.com','required':True}))
  password = forms.CharField(label='Contraseñia', widget=forms.PasswordInput,required=True)


class form_profile_veterinarian(forms.ModelForm):
  class Meta:
    model = Veterinarian

    fields =  ['dpi','name','telephone',
                'mail','address','birth_date',
                'collected_number']
    exclude = ['photo','password']

    label = {'dpi':'DPI','name':'Nombre','telephone':'Telefono',
              'mail':'Correo electronico','address':'Direccion',
              'birth_date':'Fecha nacimiento','collected_number':'Numero de colegiado'}

    widgets = {'dpi':forms.TextInput(attrs={'disabled':True}),
               'birth_date':forms.TextInput(attrs={'disabled':True}),}    
  