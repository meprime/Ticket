from django import forms
from Event.models import Event, Venue
from django.utils.translation import ugettext_lazy as _


class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer']
        labels = {
            'title': _('عنوان'),
            'description': _('توضیحات'),
            'venue': _('مکان'),
            'type': _('دسته'),
            'sub_type': _('زیردسته'),
        }


class NewVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        exclude = []
        labels = {
            'name': _('نام'),
            'address': _('آدرس'),
        }