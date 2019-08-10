from django.shortcuts import render
from django.views.generic import CreateView
from .models import pet_appointment
from .forms import post_form_medical_appointment

# Create your views here.
def index(request):
    return render(request,'pet_care/standard_pages/index.html',{})

def medical_appointment(request):
    form = post_form_medical_appointment()
    return render(request, 'pet_care/user/medical_appointment.html', {'form':form})