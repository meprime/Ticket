from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Ticket.views.index'),
    url(r'^contact/$', 'Ticket.views.contact_us'),
    url(r'^event/', 'Event.views.single_event'),
    url(r'^organizer-event/', 'Event.views.organizer_event'),  # LATER COULD BE MERGED WITH EVENT
    url(r'^new-event/', 'Event.views.new_event'),
    url(r'^my-tickets/', 'Ticket.views.user_tickets'),
]
