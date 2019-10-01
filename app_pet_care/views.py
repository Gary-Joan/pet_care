from django.shortcuts import render, redirect

from .forms import *
from .models import Event, Veterinarian
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
from .utils import Calendar
import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from CitaLog.models import EventCita
from django.db.models import Count

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
        user = Veterinarian.objects.get(id=request.session.get('id_veterinarian'))
        if(request.session.get('id_veterinarian') == ''):
            return render(request, 'pet_care/standard_pages/index.html', {}) 
        else:
            form = form_home_veterinarian(instance = user)
            welcome = 'Bienvenido ' + user.name
            
            if user.photo != None:
                image = user.photo
            else:
                image = "#"
            context={'welcome':welcome,'image':image,'form':form} 
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
        return redirect('cal:index_veterinarian')
    else:
        return redirect('cal:index_veterinarian')
        
def top10_dog_breeds(request):
    if request.session.get('id_veterinarian') != None:
        races = EventCita.objects.values('race').annotate(total=Count('race')).order_by('-total')[:10]
        counter = 1
        return render(request,'pet_care/veterinarian/top10_dog_breeds.html',{'lista':races,'counter':counter})
    else:
        return redirect('cal:index_veterinarian')


#ADMINISTRATOR
def index_administrator(request):
    if request.POST:
        form = login_administrador(request.POST)
        if form.is_valid():
            
            user = form.cleaned_data.get("user")
            password = form.cleaned_data.get("password")

            if user == "administrador" and password == "1234":        
                request.session["id_administrator"] = "administrador"
                return redirect('cal:home_administrator')
            else:
                msg = "Contraseñia invalida"
                context={'form':form,'msg':msg}
                return render(request, 'pet_care/administrator/index.html', context)    
    else:
        form = login_administrador()
        msg = ""
        context={'form':form,'msg':msg}
        return render(request, 'pet_care/administrator/index.html', context)

def logout_administrador(request):
    if request.session.get('id_administrator') != None:
        del request.session["id_administrator"]
        return redirect('cal:index_administrator')
    else:
        return redirect('cal:index_administrator')


def home_administrator(request):
    return render(request,"pet_care/administrator/home.html",{})
    if request.session.get('id_administrator') != None:
        if(request.session.get('id_administrator') == ''):
            return render(request, 'pet_care/standard_pages/index.html', {}) 
        else:
            welcome = 'Bienvenido administrador' 
            return render(request,"pet_care/administrator/home.html",{'welcome':welcome})
    else:
        return redirect('cal:index')

def new_veterinarian(request):
    if request.session.get('id_administrator') != None:
        data = request.POST.copy()

        user = Veterinarian.objects.get(dpi = data.get('dpi'))
        form = new_veterinarian_form(request.POST,request.FILES)
        
        if request.POST and user == None:
            if form.is_valid():
                form.save()
            welcome = 'Bienvenido administrador'
            return render(request,'pet_care/administrator/home.html',{'welcome':welcome})

        elif request.POST:
            return render(request,'pet_care/administrator/new_veterinarian.html',{'form':form})

        else:
            form = new_veterinarian_form()
            return render(request,'pet_care/administrator/new_veterinarian.html',{'form':form})
    else:
        return redirect('cal:index')
        
def update_veterinarian(request):
    if request.session.get('id_administrator') != None:
        lista = Veterinarian.objects.all()

        if request.POST:
            id = request.POST['user_value']
            user = Veterinarian.objects.get(id = id)
            form = form_profile_veterinarian(instance=user)
            context = {'form':form}
            return render(request,"pet_care/administrator/profile_veterinarian.html",context)         
        else:
            context = {'list':lista}
            return render(request,"pet_care/administrator/update_veterinarian.html",context)    
    
    else:
        return redirect('cal:index')

def save_profile_veterinarian_administrator(request):
    if request.session.get('id_administrator') != None:
        data = request.POST.copy()
        
        user = Veterinarian.objects.get(mail = data.get('mail'))
        form = form_profile_veterinarian(request.POST,instance=user)
        if request.POST:
            if form.is_valid():
                form.save()
        
        return redirect('cal:update_veterinarian')
    else:
        return redirect('cal:index')

def delete_veterinarian(request):
    if request.session.get('id_administrator') != None:
        
        if request.POST:
            id = request.POST['user_value']
            Veterinarian.objects.filter(id = id).delete()

        lista = Veterinarian.objects.all()
        context = {'list':lista}
        return render(request,"pet_care/administrator/delete_veterinarian.html",context)
    else:
        return redirect('cal:index')   