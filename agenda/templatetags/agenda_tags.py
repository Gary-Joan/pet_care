from django.template import Library
from django.core.urlresolvers import reverse
from agenda.models import  Event, Agenda
import datetime

today = datetime.date.today()

TIMES = {'all': None,
         'this_month': today.month,
         'last_month': today.month - 1,
         'year': today.year
         }
register = Library()

@register.inclusion_tag('agenda/tags/dummy.html')
def event_list_for(instance, element_number = 10, template='agenda/tags/event_list.html', limit='all',):
    if limit=='this_month':
        events = Event.objects.find_by_owner(instance).filter(start__month = TIMES[limit])[:element_number]
    elif limit=='last_month':
        events = Event.objects.find_by_owner(instance).filter(start__month = TIMES[limit])[:element_number]
    elif limit== 'year':
        events = Event.objects.find_by_owner(instance).filter(start__year= TIMES[limit])[:element_number]
    else:
        events = Event.objects.find_by_owner(instance)[:element_number]

    return {'template': template, 
            'events': events}

@register.inclusion_tag('agenda/tags/dummy.html')
def public_event_list(element_number = 10, template='agenda/tags/event_list.html'):
    events = Event.objects.filter(status = 1)[:element_number]
    return {'template': template, 
            'events': events}

@register.filter
def get_agenda_url(instance, **kwargs):
    agenda = Agenda.objects.find_by_owner(instance)
    if instance._meta.object_name=='User' and agenda.count() == 0:
        if instance.has_agenda == False:
            agenda = instance.create_my_agenda()
            instance.save()
    elif agenda.count()==0: 
        raise Exception("Agenda not found for instance: %s" % instance)

    return reverse('agenda_view_date', args=[agenda[0].id]) 
