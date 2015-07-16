from django.db import models
from User.models import EventOrganizer, Customer
from django.core.exceptions import ValidationError


class Venue(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=80)
    # decompose address as city, street, number


class Type(models.Model):
    name = models.CharField(max_length=20)


class SubType(models.Model):
    name = models.CharField(max_length=40)
    type = models.ForeignKey(Type)


class Event(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    date_time = models.DateTimeField
    # img =
    venue = models.ForeignKey(Venue)
    type = models.ForeignKey(Type)
    sub_type = models.ForeignKey(SubType)
    organizer = models.ForeignKey(EventOrganizer)

    def clean(self):
        super(self)
        if SubType.objects.get(id=self.sub_type).type_id != self.type:
            raise ValidationError('sub_type should actually be a sub-type of type!')


class Ticket(models.Model):
    event = models.ForeignKey(Event)
    type = models.CharField(max_length=20)
    capacity = models.IntegerField
    sold = models.IntegerField
    price = models.IntegerField


class BoughtTicket(models.Model):
    ticket = models.ForeignKey(Ticket)
    buyer = models.ForeignKey(Customer)
    serial_no = models.BigIntegerField


