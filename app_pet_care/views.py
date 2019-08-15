from django.shortcuts import render, redirect

from .forms import *
from .models import Event, Veterinarian
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from django.utils.safestring import mark_safe
from .utils import Calendar
import calendar

# Create your views here.
def index(request):
    return render(request, 'pet_care/standard_pages/index.html', {})
def indexCliente(request):
    return render(request, 'pet_care/user/cliente.html', {})

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

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
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:event_new'))
    return render(request, 'cal/event.html', {'form': form})


#VETERINARIAN
def index_veterinarian(request):
    if request.POST:
        form = login_veterinarian(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("user")
            password = form.cleaned_data.get("password")
            try:
                System_User = Veterinarian.objects.get(mail = user)
                
                
                if password == System_User.password:
                    
                    request.session["id_veterinarian"] = System_User.id
                    return redirect('cal:home_veterinarian')
                else:
                    msg = "Contraseñia invalida"
                    context={'form':form,'msg':msg}
                    return render(request, 'pet_care/veterinarian/index.html', context)    

            except Exception as e:
                msg = "Usuario invalido"
                context={'form':form,'msg':msg}
                return render(request, 'pet_care/veterinarian/index.html', context)
            
    else:
        form = login_veterinarian()
        msg = ""
        context={'form':form,'msg':msg}
        return render(request, 'pet_care/veterinarian/index.html', context) 
        
def home_veterinarian(request):
    if request.session.get('id_veterinarian') != None:
        if(request.session.get('id_veterinarian') == ''):
            return render(request, 'pet_care/standard_pages/index.html', {}) 
        else:
            user = Veterinarian.objects.get(id=request.session.get('id_veterinarian'))
            image = user.photo
            print(image)
            welcome = 'Bienvenido ' + user.name
            context={'welcome':welcome,'image':image}
            return render(request,"pet_care/veterinarian/home.html",context)
    else:
        return redirect('cal:index')

def profile_veterinarian(request):
    if request.session.get('id_veterinarian') != None:
        user = Veterinarian.objects.get(id=request.session.get('id_veterinarian'))
        if request.POST:  
            form = form_profile_veterinarian(request.POST, instance = user)
            if form.is_valid():
                form.save()

            return render(request, 'pet_care/veterinarian/profile.html', {'form':form})
        else:        
            form = form_profile_veterinarian(instance = user)
            return render(request, 'pet_care/veterinarian/profile.html', {'form':form})
    else:
        return redirect('cal:index')
    
def logout_veterinarian(request):
    if request.session.get('id_veterinarian') != None:
        del request.session["id_veterinarian"]
        return redirect('cal:index')
    else:
        return redirect('cal:index')
        
