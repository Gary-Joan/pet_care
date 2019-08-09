"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *
import datetime
import time
from django.utils import simplejson
from django.contrib.auth.models import User

class EventTest(TestCase):

    fixtures = ['initial_data.json']

    def test_event_to_json(self):
        '''Test the convertion of an event to json'''
        user = User.objects.all()[0]
        agenda = Agenda(name='test agenda',
                            owner = user,
                            public=True)
        agenda.save()
        start = datetime.datetime(2010, 10, 11, 10, 10)
        end = datetime.datetime(2010, 10, 12, 10, 10)
        kwargs = {'title': 'test',
                 'description': 'test event',
                 'start': start,
                 'end': end, 
                 'owner': user,
                 'created_on': start,
                 'agenda': agenda
                 }
        event = Event(**kwargs)
        json = dict.copy(kwargs)
        json['start'] = time.mktime(start.timetuple())
        json['created_on'] = time.mktime(start.timetuple())
        json['end'] = time.mktime(end.timetuple())
        json['owner'] = user.username
        json['agenda'] = agenda.id
        json['shared'] = False
        json['id'] = None
        
        
        self.assertEqual(event.to_json(), simplejson.dumps(json))

    def test_event_to_dict(self):
        '''Test the convertion of an event to json'''
        user = User.objects.all()[0]
        agenda = Agenda(name='test agenda',
                            owner = user,
                            public=True)
        agenda.save()
        start = datetime.datetime(2010, 10, 11, 10, 10)
        end = datetime.datetime(2010, 10, 12, 10, 10)
        kwargs = {'title': 'test',
                 'description': 'test event',
                 'start': start,
                 'end': end, 
                 'owner': user,
                 'created_on': start,
                 'agenda': agenda
                 }
        event = Event(**kwargs)
        json = dict.copy(kwargs)
        json['start'] = time.mktime(start.timetuple())
        json['created_on'] = time.mktime(start.timetuple())
        json['end'] = time.mktime(end.timetuple())
        json['owner'] = user.username
        json['agenda'] = agenda.id
        json['shared'] = False
        json['id'] = None
        
        
        self.assertEqual(event.to_dict(), json)


