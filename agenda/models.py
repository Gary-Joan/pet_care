from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.utils import simplejson
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from agenda.managers import AgendaManager, EventManager

import datetime
import time

STATUS_CHOICES = (('1', _('Public')),
                  ('2', _('Registered Users')),
                  ('3', _('Restricted')),
                  ('4', _('Private')))

class Agenda(models.Model):
    name = models.CharField(max_length=100)
    public = models.BooleanField(default=False)

    #any model can have it's on agenda that's the owner
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objects = AgendaManager()

    def get_events(self, start, end):
        return Event.objects.filter(start__gt = start, 
                end__lt = end, agenda = self)

    def get_shared_events(self, start, end, user):
        return EventInvite.objects.filter(event__start__gt = start, 
                event__end__lt = end, to_user__username = user)

    def is_owner(self, owner):
        owner_content_type = ContentType.objects.get_for_model(owner)
        return self.content_type.id == owner_content_type.id and self.object_id == owner.id

    def __unicode__(self):
        return '%s' % (self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('agenda_view_date' (self.id,))

    class Meta:
        verbose_name = _('agenda')
        unique_together = ('object_id', 'content_type')

class Event(models.Model):
    '''Event class to make a simple event 
       inspired in django-schedule'''
    title = models.CharField(_('title'), max_length=200)
    description = models.TextField(_('description'), blank=True)
    start = models.DateTimeField(_('start'), default=datetime.datetime.now())
    end = models.DateTimeField(_('end'))
    created_on = models.DateTimeField(_('created_on'), auto_now = True)
    agenda = models.ForeignKey(Agenda)
    status = models.CharField(_('status'), choices = STATUS_CHOICES, 
                              max_length=1,
                              help_text=_('''Public - visible for everyone, 
                              Registered Users: visible for registered users, 
                              Restricted: visible just for invited people, 
                              Private: visible just for you'''))

    objects = EventManager()

    def can_be_viewed(self, user):
        '''checks if a user can view a event'''
        if user.is_authenticated():
            if self.status == '4': #private
                return self.agenda.is_owner(user)
            elif self.status == '3': #invited only
                return self.is_invited(user)
            elif self.status <= '2': #registered and public
                return True
            else:
                return False
        else:
            return self.status == '1'

    def can_be_shared_by(self, user):
        if user.is_authenticated():
            if self.status in (1, 2):
                return True
            elif self.status in (3,4):
                return self.agenda.is_owner(user)

    @models.permalink
    def get_absolute_url(self):
        return ('agenda_event_detail' (self.id,))

    def is_invited(self, user):
        if EventInvite.objects.get(to_user = user, event = self):
            return True
        else:
            return False

    def __unicode__(self):
        return self.title

    def to_dict(self):
        dicc = {
                'id': self.id,
                'title': self.title,
                'description': self.description,
                'start': time.mktime(self.start.timetuple()),
                'end': time.mktime(self.end.timetuple()),
                'created_on': time.mktime(self.created_on.timetuple()),
                'agenda': self.agenda.id,
                'shared': False,
                }
        return dicc

    def to_json(self):
        return simplejson.dumps(self.to_dict())

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
        ordering = ('-start',)

#class SharedEvent(models.Model):
#    '''Intermediate model to share events
#       the new_event field is used as flag for 
#       notifications'''
#    event = models.ForeignKey(Event)
#    participant = models.ForeignKey(User)
#    attending = models.BooleanField(default=False)
#    new_event = models.BooleanField(default=True)
#
#    def __unicode__(self):
#        return '%s - %s - %s' % (self.event.title, 
#                self.participant, self.attending)
#
#    def get_absolute_url(self):
#        pass
#
#    def to_dict(self):
#        dicc = {
#                'id': self.event.id,
#                'title': self.event.title,
#                'description': self.event.description,
#                'start': time.mktime(self.event.start.timetuple()),
#                'end': time.mktime(self.event.end.timetuple()),
#                'created_on': time.mktime(self.event.created_on.timetuple()),
#                'agenda': self.event.agenda.id,
#                'shared': True,
#                'attending': self.attending,
#                'new_event': self.new_event,
#                'className': 'fc-shared-event',
#                }
#        return dicc
#
#    def to_json(self):
#        return simplejson.dumps(self.to_dict())
#
#    def unflag(self):
#        self.new_event = False
#
#    class Meta:
#        verbose_name = _('shared event')
#        verbose_name_plural = _('shared event')

class EventInvite(models.Model):
    '''This is the invite to a event'''
    from_user = models.ForeignKey(User)
    to_user = models.ForeignKey(User, related_name = 'to_user')
    event = models.ForeignKey(Event)
    date_created = models.DateTimeField(auto_now_add = True) 

    attending = models.BooleanField(default=False)
    new_event = models.BooleanField(default=True)

    def __unicode__(self):
        return _("%s invito %s para el evento %s" % (self.from_user.username, 
                self.to_user.username, self.event.title)) 

    def clean(self):
       '''Does not allows that from user is the same to user'''
       from django.core.exceptions import ValidationError
       if self.from_user == self.to_user:
           raise ValidationError('You can not invite yourself')

    def save(self, *args, **kwargs):
        super(EventInvite, self).save(*args, **kwargs)

    def to_dict(self):
        dicc = {
                'id': self.event.id,
                'title': self.event.title,
                'description': self.event.description,
                'start': time.mktime(self.event.start.timetuple()),
                'end': time.mktime(self.event.end.timetuple()),
                'created_on': time.mktime(self.event.created_on.timetuple()),
                'agenda': self.event.agenda.id,
                'shared': True,
                'attending': self.attending,
                'new_event': self.new_event,
                'className': 'fc-shared-event',
                }
        return dicc

    def to_json(self):
        return simplejson.dumps(self.to_dict())

    def unflag(self):
        self.new_event = False

    class Meta:
        verbose_name = _('Event Invite')
        verbose_name_plural = _('Event Invites')
        unique_together = ('event', 'to_user')
        ordering = ['-date_created', 'new_event']
