from django.conf.urls.defaults import url 
from django.conf.urls.defaults import patterns 
from django.conf import settings

urlpatterns = patterns('agenda.views',
    url(r'^agenda/(?P<agenda_id>\d+)/$', 'view_date', name='agenda_view_date'),
    url(r'^event/(?P<event_id>\d+)/$', 'event_detail', name='agenda_event_detail'),
    url(r'^event/(?P<event_id>\d+)/delete/$', 'delete_event', name='agenda_event_delete'),
    url(r'^event/(?P<event_id>\d+)/edit/$', 'edit_event', name='agenda_event_edit'),
    url(r'^event/(?P<event_id>\d+)/invite/$', 'share_event', name='agenda_event_share'),
    url(r'^event/event/inbox/$', 'event_inbox', name='agenda_event_inbox'),
    url(r'^agenda/(?P<agenda_id>\d+)/new/$', 'create_event', name='agenda_event_create'),
)
