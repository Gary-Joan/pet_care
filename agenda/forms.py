from django import forms as forms
from django.forms.extras.widgets import *
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from models import *

class EventForm(forms.ModelForm):
    agenda = forms.ModelChoiceField(widget = forms.HiddenInput(), required=False, queryset=Agenda.objects.all())
    
    class Meta:
        model = Event 

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda 

class EventInviteForm(forms.Form):
    users = forms.ModelMultipleChoiceField(queryset= User.objects.all())

class AgendaAdminForm(forms.ModelForm):
    object_id = forms.ChoiceField(label=_('object'), choices=(('','----'),('1', '------')))

    def __init__(self, *args, **kwargs):
        super(AgendaAdminForm, self).__init__(*args, **kwargs)
        self.fields['content_type'] = forms.ModelChoiceField(queryset = ContentType.objects.filter(**self.get_params_for_content_type()))

    class Meta:
        model = Agenda

    def get_params_for_content_type(self):
        app_labels = []
        models = []
        for full_model in settings.AGENDA_AUTHORIZED_MODELS:
            label, model = full_model.split('.')
            app_labels.append(label)
            models.append(model)

        return dict(app_label__in = app_labels, model__in = models)
