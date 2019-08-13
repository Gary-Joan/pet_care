from django.forms import ModelForm, DateInput, TimeInput
from .models import EventCita


class EventForm(ModelForm):
  class Meta:
    model = EventCita
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
        'start_time': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),

        'date_start_time': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        'date_end_time': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field

    self.fields['start_time'].input_formats = ('%Y-%m-%d',)

    self.fields['date_start_time'].input_formats = ('%H:%M',)
    self.fields['date_end_time'].input_formats = ('%H:%M',)


    self.fields['doctor'].label = "Nombre Veterinario"
    self.fields['title'].label = "Nombre Mascota"