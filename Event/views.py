from django.shortcuts import render
from Ticket.forms import *


def single_event(request):
    pass


def organizer_event(request):
    ticket_form = NewTicketTypeForm
    update_event_form = UpdateEventForm(  # needs to be taken care of
        initial={
            'description': 'یک مسابقه‌ی هیجان‌انگیز',
            }
    )
    return render(request, 'organizer_event.html', {
        'ticket_form': ticket_form,
        'update_event_form': update_event_form,
    })


def new_event(request):
    event_form = NewEventForm
    venue_form = NewVenueForm
    return render(request, 'new_event.html', {
        'event_form': event_form,
        'venue_form': venue_form,
    })