from django.shortcuts import render

# Create your views here.
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar

from .models import EventCita
from .utils import Calendar
from .forms import EventForm

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