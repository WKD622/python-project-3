# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import SuspiciousOperation
from django.db import transaction
from django.db.models.aggregates import Max
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, reverse

from howdy.models import Employee
from howdy.models import Income
from howdy.models import Outcome


# łaczy strone z template
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class AboutPageView(TemplateView):
    template_name = "about.html"


def index(request):
    return render(request, 'index.html')

    # elif request.method == "GET":
    #     return render(request, 'index.html', {'text2': request.GET.get('muisend', 'krowa')})
    # employees = Employee.objects.all().values('first_name', 'pesel')
    # return render(request, 'index.html', {'text': sent, 'employees': employees})


def add_to_database(request):
    if request.method == "POST":
        name_e = request.POST.get('name_e')
        last_name_e = request.POST.get('last_name_e')
        pesel_e = request.POST.get('pesel_e')
        salary_e = request.POST.get('salary_e')

        sum_i = request.POST.get('sum_i')
        name_i = request.POST.get('name_i')
        date_i = request.POST.get('date_i')

        sum_o = request.POST.get('sum_o')
        name_o = request.POST.get('name_o')
        date_o = request.POST.get('date_o')

        if name_e is not None and last_name_e is not None and pesel_e is not None and salary_e is not None:
            employee = Employee(first_name=name_e, last_name=last_name_e, pesel=pesel_e, salary=salary_e)
            employee.save()

        if name_i is not None and sum_i is not None and date_i is not None:
            income = Income(sum=sum_i, date=date_i, name=name_i)
            income.save()

        if name_o is not None and sum_o is not None and date_o is not None:
            outcome = Outcome(sum=sum_o, date=date_o, name=name_o)
            outcome.save()

    return render(request, 'add_to_database.html')


def manage_employees(request):
    return render(request, 'manage_employees.html')


def manage_expenditures(request):
    return render(request, 'manage_expenditures.html')


def manage_incomes(request):
    return render(request, 'manage_incomes.html')

