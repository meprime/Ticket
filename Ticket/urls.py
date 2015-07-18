from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Ticket.views.index'),
    url(r'^contact/$', 'Ticket.views.contact_us'),
    url(r'^event/', 'Event.views.single_event'),
    url(r'^new_event/', 'Event.views.new_event'),
]
