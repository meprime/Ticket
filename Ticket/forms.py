from django import forms
from Event.models import Event, Venue, Ticket
from django.utils.translation import ugettext_lazy as _


class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer']
        labels = {
            'title': _('عنوان'),
            'description': _('توضیحات'),
            'date': _('تاریخ'),
            'time': _('زمان'),
            'venue': _('مکان'),
            'type': _('دسته'),
            'sub_type': _('زیردسته'),
        }


class UpdateEventForm(forms.ModelForm):  # used for organizer to update some properties of her event
    class Meta:
        model = Event
        fields = ['description', 'date', 'time', 'venue']
        labels = {
            'description': _('توضیحات'),
            'date': _('تاریخ'),
            'time': _('زمان'),
            'venue': _('مکان'),
        }


class NewVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        exclude = []
        labels = {
            'name': _('نام'),
            'address': _('آدرس'),
        }


class NewTicketTypeForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['event', 'sold']
        labels = {
            'type': _('نوع'),
            'capacity': _('ظرفیت'),
            'price': _('قیمت'),
        }


class UserUpdateForm(forms.Form):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), required=True, label='رمز عبور جدید')
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput(), required=True, label='تأیید رمز عبور')
    nl_memb = forms.BooleanField(label='عضویت در خبرنامه')  #newsletter membership
