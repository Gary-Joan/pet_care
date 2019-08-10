from django.shortcuts import render
from django.views.generic import CreateView
from .models import pet_appointment
from .forms import post_form_medical_appointment

# Create your views here.
def index(request):
    return render(request,'pet_care/standard_pages/index.html',{})

def medical_appointment(request):
    if request.method == "POST":
        form = post_form_medical_appointment(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.nombreMascota=request.form_name
            post.save()
    else:
        form = post_form_medical_appointment()
    return render(request, 'pet_care/user/medical_appointment.html', {'form':form})