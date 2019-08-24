from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ClientProfile, GradeMedic

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = {'username', 'email', 'first_name', 'last_name', 'password1', 'password2'}

    def save(self, commit=True):
        user =super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class UserProfileForm(ModelForm):
    class Meta:
        model = ClientProfile
        fields = {'address', 'phone'}

class form_doctor_grade(forms.ModelForm):
  class Meta:
    model = GradeMedic

    fields = '__all__'

    labels = {'client_name': 'Nombre Cliente', 'doctor_name': 'Nombre Doctor', 'grade_doctor': 'Calificacion'}

