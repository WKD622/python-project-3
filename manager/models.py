from __future__ import unicode_literals
from datetime import datetime
from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11)
    position = models.CharField(max_length=50, null=True)
    salary = models.IntegerField(null=True)


class Income(models.Model):
    sum = models.IntegerField(null=True)
    date = models.DateField(default=datetime.now, blank=True)
    name = models.CharField(max_length=50)


class Outcome(models.Model):
    sum = models.IntegerField(null=True)
    date = models.DateField(default=datetime.now, blank=True)
    name = models.CharField(max_length=50)


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True)
    date = models.DateField(blank=True)
    time = models.TimeField(null=True)
