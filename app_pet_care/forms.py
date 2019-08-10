from django import forms
from .models import pet_appointment

class post_form_medical_appointment(forms.ModelForm):
    form_name = forms.CharField(label='Nombre de mascota',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'mascota', 'required': True}))
    form_date = forms.DateField(label='Fecha', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}))
    form_hour = forms.DateTimeField(label='Hora', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'time', 'required': True}))

    class Meta:
        model = pet_appointment
        fields = ('form_name', 'form_date', 'form_hour')