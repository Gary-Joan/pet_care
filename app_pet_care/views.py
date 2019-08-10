from django.shortcuts import render

from .forms import post_form_medical_appointment
from .models import pet_appointment

# Create your views here.
def index(request):
    return render(request, 'pet_care/standard_pages/index.html', {})

def medical_appointment(request):
        form = post_form_medical_appointment(request.POST or None)
        if form.is_valid():
            form_data = form.cleaned_data
            nombreMascota = form_data.get("form_name")
            print(form_data.get("form_name"))
            FechaCita =  form_data.get("form_date")
            Hora = form_data.get("form_hour")
            obj = pet_appointment.objects.create(pet_name=nombreMascota, date=FechaCita, hour=Hora)

        return render(request, 'pet_care/user/medical_appointment.html', {'form': form})

