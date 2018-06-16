from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import SuspiciousOperation
from django.db import transaction
from django.db.models.aggregates import Max
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.db.models import Count
from django.db.models import Sum

from manager.models import Employee
from manager.models import Income
from manager.models import Outcome


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def index(request):
    return render(request, 'index.html')


def add_to_database(request):
    if request.method == "POST":
        name_e = request.POST.get('name_e')
        last_name_e = request.POST.get('last_name_e')
        pesel_e = request.POST.get('pesel_e')
        salary_e = request.POST.get('salary_e')
        position_e = request.POST.get('position_e')

        sum_i = request.POST.get('sum_i')
        name_i = request.POST.get('name_i')
        date_i = request.POST.get('date_i')

        sum_o = request.POST.get('sum_o')
        name_o = request.POST.get('name_o')
        date_o = request.POST.get('date_o')

        if name_e is not None and last_name_e is not None and pesel_e is not None and salary_e is not None and position_e is not None:
            employee = Employee(first_name=name_e, last_name=last_name_e, pesel=pesel_e, salary=salary_e, position=position_e)
            employee.save()

        if name_i is not None and sum_i is not None and date_i is not None:
            income = Income(sum=sum_i, date=date_i, name=name_i)
            income.save()

        if name_o is not None and sum_o is not None and date_o is not None:
            outcome = Outcome(sum=sum_o, date=date_o, name=name_o)
            outcome.save()

    return render(request, 'add_to_database.html')


def manage_employees(request):
    employees = Employee.objects.order_by('-salary')[:5]
    cost = Employee.objects.aggregate(Sum('salary'))
    return render(request, 'manage_employees.html', {'employees': employees, 'cost': cost})


def manage_expenditures(request):
    expenditures = Outcome.objects.order_by('-date')[:5]
    sum = Outcome.objects.aggregate(Sum('sum'))
    return render(request, 'manage_expenditures.html', {'expenditures': expenditures, 'sum': sum})


def manage_incomes(request):
    incomes = Income.objects.order_by('-date')[:5]
    sum = Income.objects.aggregate(Sum('sum'))
    return render(request, 'manage_incomes.html', {'incomes': incomes, 'sum': sum})


def see_all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'see_all_employees.html', {'employees': employees})


def fire_employee(request):
    if request.method == "POST":
        pesel_e = request.POST.get('pesel_e')
        Employee.objects.filter(pesel=pesel_e).delete()

    return render(request, 'fire_employee.html')


def promote_employee(request):
    if request.method == "POST":
        pesel_e = request.POST.get('pesel_e')
        salary_e = request.POST.get('salary_e')
        promotion = Employee.objects.get(pesel = pesel_e)
        promotion.salary = salary_e
        promotion.save()

    return render(request, 'promote_employee.html')


def see_all_incomes(request):
    incomes = Income.objects.all().order_by('-date')
    return render(request, 'see_all_incomes.html', {'incomes': incomes})


def see_all_expenditures(request):
    expenditures = Outcome.objects.all().order_by('-date')
    return render(request, 'see_all_expenditures.html', {'expenditures': expenditures})