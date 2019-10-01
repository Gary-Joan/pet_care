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
    self.fields['start_time'].label = "Fecha y hora a reservar"

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

class login_administrador(forms.Form):
  user = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'placeholder':'username','required':True}))
  password = forms.CharField(label='Contraseñia', widget=forms.PasswordInput,required=True)


class new_veterinarian_form(forms.ModelForm):
  class Meta:
    model = Veterinarian

    fields =  [
      'name','telephone',
      'mail','address',
      'collected_number',
      'photo',
      'password',
      'birth_date',
      'dpi'
    ]

    labels = {
      'name':'Nombre',
      'dpi':'DPI',
      'telephone':'Telefono',
      'mail':'Correo electronico',
      'address':'Direccion',
      'collected_number':'Numero de colegiado',
      'photo':'Seleccione una foto',
      'birth_date':'Fecha de nacimiento',
      'password':'Contraseñia'
    } 

    widgets ={
      'name':forms.TextInput(attrs={'required':True}),
      'dpi':forms.TextInput(attrs={'required':True}),
      'telephone':forms.TextInput(attrs={'required':True}),
      'mail':forms.TextInput(attrs={'required':True}),
      'address':forms.TextInput(attrs={'required':True}),
      'collected_number':forms.TextInput(attrs={'required':True}),
      'password':forms.PasswordInput(attrs={'required':True}),
      'birth_date':forms.DateInput(attrs={'required':True}),
    }

