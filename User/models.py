from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    user = models.OneToOneField(User)


class Customer(models.Model):
    user = models.OneToOneField(User)
    nl_memb = models.BooleanField # newsletter membership


class EventOrganizer(models.Model):
    user = models.OneToOneField(User)
    is_active = models.BooleanField(default=False)
