from django.db.models import Manager
from django.contrib.contenttypes.models import ContentType

class AgendaManager(Manager):
    '''manager to find by owner'''

    def find_by_owner(self, owner):
        '''where owner is the instance of the owner'''
        owner_content_type = ContentType.objects.get_for_model(owner)
        return self.get_query_set().filter(content_type__pk = owner_content_type.id, 
                                           object_id = owner.id) 

class EventManager(Manager):
    '''finding by owner'''

    def find_by_owner(self, owner):
        '''where owner is the instance of the owner'''
        owner_content_type = ContentType.objects.get_for_model(owner)
        return self.get_query_set().filter(agenda__content_type__pk = owner_content_type.id, 
                                           agenda__object_id = owner.id) 
