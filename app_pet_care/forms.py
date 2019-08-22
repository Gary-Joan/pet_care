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
    self.fields['doctor'].label = "Doctor que atiende"
    self.fields['pet_owner'].label = "Dueño de la mascota"
    self.fields['race'].label = "Raza de la mascota"
    self.fields['pet_sym'].label = "Simtomas descritos"
    self.fields['prescription'].label = "Preescripciones"
    self.fields['start_time'].label = "FECHA DE LA CITA"
    self.fields['date_start_time'].label = "HORA INICIO CITA"
    self.fields['date_end_time'].label = "HORA FIN CITA"

class login_veterinarian(forms.Form):
  user = forms.EmailField(label='Usuario', widget=forms.TextInput(attrs={'placeholder':'corre@correo.com','required':True}))
  password = forms.CharField(label='Contraseñia', widget=forms.PasswordInput,required=True)

class form_home_veterinarian(forms.ModelForm):
  class Meta:
    model = Veterinarian

    fields =  [
      'name','telephone',
      'mail','address',
      'collected_number'
    ]

    exclude = [
      'photo',
      'password',
      'birth_date',
      'dpi'
    ]

    labels = {
      'name':'Nombre',
      'telephone':'Telefono',
      'mail':'Correo electronico',
      'address':'Direccion',
      'collected_number':'Numero de colegiado'
    } 

    widgets ={
      'name':forms.TextInput(attrs={'disabled':True,'required':False}),
      'telephone':forms.TextInput(attrs={'disabled':True,'required':False}),
      'mail':forms.TextInput(attrs={'disabled':True,'required':False}),
      'address':forms.TextInput(attrs={'disabled':True,'required':False}),
      'collected_number':forms.TextInput(attrs={'disabled':True,'required':False})
    }
    
class form_profile_veterinarian(forms.ModelForm):
  class Meta:
    model = Veterinarian

    fields = [
      'dpi',
      'name',
      'telephone',
      'mail',
      'address',
      'collected_number',
      'birth_date',
    ]

    exclude = ['password','photo']

    labels = {
      'dpi':'DPI',
      'name':'Nombre',
      'telephone':'Telefono',
      'mail':'E-mail',
      'address':'Direccion',
      'collected_number':'Numero de colegiado',
      'birth_date':'Fecha de nacimiento',
    }