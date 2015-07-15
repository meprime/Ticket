from django.db import models
from Event.models import Event
from User.models import Customer, EventOrganizer


class Comment(models.Model):
    commenter = models.ForeignKey(Customer)
    event = models.ForeignKey(Event)
    text = models.TextField


class CommentResponse(models.Model):
    responder = models.ForeignKey(EventOrganizer)
    text = models.TextField
