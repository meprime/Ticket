from django.shortcuts import render
from Ticket.forms import NewEventForm, NewVenueForm


def single_event(request):
    pass


def new_event(request):
    event_form = NewEventForm
    venue_form = NewVenueForm
    return render(request, 'new_event.html', {
        'event_form': event_form,
        'venue_form': venue_form,
    })