from django.shortcuts import render, redirect
from CitaLog.forms import UtensilioForm

# Create your views here.
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar

from .models import EventCita, Utensilio
from .utils import Calendar
from .forms import EventForm
##Agregado para poder realizar reporte
from reportlab.pdfgen import canvas
from django.http import FileResponse
import io
from django.conf import settings
#MODIFICO CHICAS
from app_pet_care.models import Veterinarian
#FIN MODIFICACION

def index(request):
    return render(request, 'index.html', {})


class CalendarView(generic.ListView):
    model = EventCita
    template_name = 'cita/calendarC.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = EventCita()
    if event_id:
        instance = get_object_or_404(EventCita, pk=event_id)
    else:
        instance = EventCita()

    #form = EventForm(request.POST or None, instance=instance)#CODIGO ORIGINAL
    
    #MODIFICO CHICAS
    if request.session.get('id_veterinarian') != None:
        user = Veterinarian.objects.get(id=request.session.get('id_veterinarian'))
        form = EventForm(request.POST or None, instance=instance, initial={'doctor_name':user.name})
    else:
        form = EventForm(request.POST or None, instance=instance)
    #FIN MODIFICACION

    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cita:calendarC'))
    return render(request, 'cita/eventC.html', {'form': form})

def HistorialPorMascota(request, NombreMascota):    
    ListaCitas = EventCita.objects.filter(title=NombreMascota)
    return render(request, 'Historial/HistorialMascota.html', {'ListaCitas':ListaCitas})

def HistorialPorCliente(request, NombreCliente):
    ListaCitas = EventCita.objects.filter(pet_owner=NombreCliente)
    return render(request, 'Historial/HistorialCliente.html', {'ListaCitas':ListaCitas})

def Historial(request):
    ListaClientes = EventCita.objects.values('pet_owner').distinct()
    ListaMascotas = EventCita.objects.values('title').distinct()
    return render(request, 'Historial/Historial.html', {'ListaClientes':ListaClientes,'ListaMascotas':ListaMascotas})

def ListaMascotas(request):
    ListaMascotas = EventCita.objects.values('title','pet_owner','race').distinct()
    return render(request, 'CRUD_Mascota/Read_Mascotas.html', {'ListaMascotas':ListaMascotas})

def ConfirmacionBorrarMascota(request, NombreCliente, NombreMascota):
    ListaMascotas = EventCita.objects.filter(pet_owner=NombreCliente, title=NombreMascota).distinct()
    return render(request, 'CRUD_Mascota/ConfirmacionBorrar_Mascotas.html', {'ListaMascotas':ListaMascotas})

def BorrarMascota(request, NombreCliente, NombreMascota, Fecha, Hora):
    EventCita.objects.filter(pet_owner=NombreCliente, title=NombreMascota, start_time=Fecha, date_start_time=Hora).delete()
    ListaMascotas = EventCita.objects.values('title', 'pet_owner', 'race').distinct()
    return render(request, 'CRUD_Mascota/Read_Mascotas.html', {'ListaMascotas':ListaMascotas})
   
def GenerarPDFInfoCita(request, NombreCliente, NombreMascota, Fecha, Hora):
    ListaCitas = EventCita.objects.filter(pet_owner=NombreCliente, title=NombreMascota, start_time=Fecha, date_start_time=Hora)
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    i = 0
    archivo_imagen = settings.MEDIA_ROOT+'\media\image_veterinarian\LogoUSAC.jpg'
    p.drawImage(archivo_imagen, 325, 650, 240, 180,preserveAspectRatio=True)
    for MiCita in ListaCitas:
        if i != 0:
            break
        i = i+1
        p.drawString(50, 750, "Doctor que atendio: " + MiCita.doctor_name)
        p.drawString(50, 730, "Dueño de mascota: " + MiCita.title)
        p.drawString(50, 710, "Mascota: " + MiCita.pet_owner)
        p.drawString(50, 690, "Raza: " + MiCita.race)
        p.drawString(50, 670, "Descripcion: ")
        i = 660
        j = 100
        linea = ""
        for letra in MiCita.description:
            if j > 500:
                j = 100
                i = i - 10
                p.drawString(j, i,linea)
                linea = ""
            linea = linea + letra
            j = j + 5
        j = 100
        i = i - 10
        p.drawString(j, i,linea)
        i = i - 20
        ########################### Sintomas #####################################
        p.drawString(50, i, "Sintomas: ")
        i = i - 10
        j = 100
        linea = ""
        for letra in MiCita.pet_sym:
            if j > 500:
                j = 100
                i = i - 10
                p.drawString(j, i,linea)
                linea = ""
            linea = linea + letra
            j = j + 5
        j = 100
        i = i - 10
        p.drawString(j, i,linea)
        i = i - 20
        ####################### Prescripcion ###################################
        p.drawString(50, i, "Prescripcion: ")
        i = i - 10
        j = 100
        linea = ""
        for letra in MiCita.prescription:
            if j > 500:
                j = 100
                i = i - 10
                p.drawString(j, i,linea)
                linea = ""
            linea = linea + letra
            j = j + 5
        j = 100
        i = i - 10
        p.drawString(j, i,linea)
        i = i - 20
        p.drawString(50, i, "Fecha: "+ MiCita.start_time.strftime("%b %d %Y")+ " Hora: "+MiCita.date_start_time.strftime("%H:%M:%S"))
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='Reporte Cita.pdf')


def ListaUtensilios(request):
    ListaUtensilios = Utensilio.objects.values('id', 'nombre', 'descripcion').distinct()
    return render(request, 'Utensilio/ListarUtensilios.html', {'ListaUtensilios':ListaUtensilios})

def CrearUtensilio(request):
    form = UtensilioForm()    
    if request.method =="POST":
        form = UtensilioForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)            
            instancia.save()
            return redirect("cita:ListaUtensilios")
    return render(request, "Utensilio/AgregarUtensilio.html", {'form': form})    

def BorrarUtensilio(request, id):
    Utensilio.objects.filter(id=id).delete()
    ListaUtensilios = Utensilio.objects.values('id', 'nombre', 'descripcion').distinct()
    return render(request, 'Utensilio/ListarUtensilios.html', {'ListaUtensilios':ListaUtensilios})