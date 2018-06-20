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
from manager.models import Event
from datetime import datetime as dt
from datetime import timedelta
import datetime


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def index(request):
    return render(request, 'index.html')


def manage_employees(request):
    if request.method == "POST":
        name_e = request.POST.get('name_e')
        last_name_e = request.POST.get('last_name_e')
        pesel_e = request.POST.get('pesel_e')
        salary_e = request.POST.get('salary_e')
        position_e = request.POST.get('position_e')
        if None and "" not in [name_e, last_name_e, pesel_e, salary_e, position_e]:
            employee = Employee(first_name=name_e, last_name=last_name_e, pesel=pesel_e, salary=salary_e,
                                position=position_e)
            employee.save()

    employees = Employee.objects.order_by('-salary')[:5]
    cost = Employee.objects.aggregate(Sum('salary'))
    return render(request, 'manage_employees.html', {'employees': employees, 'cost': cost})


def manage_expenditures(request):
    if request.method == "POST":
        sum_o = request.POST.get('sum_o')
        name_o = request.POST.get('name_o')
        date_o = request.POST.get('date_o')
        if None or "" not in [name_o, sum_o, date_o]:
            outcome = Outcome(sum=sum_o, date=date_o, name=name_o)
            outcome.save()

    expenditures = Outcome.objects.order_by('-date')[:10]
    sum = Outcome.objects.aggregate(Sum('sum'))
    sum_month = Outcome.objects.filter(date__gte=dt.today() - timedelta(days=30)).aggregate(Sum('sum'))
    sum_week = Outcome.objects.filter(date__gte=dt.today() - timedelta(days=7)).aggregate(Sum('sum'))
    return render(request, 'manage_expenditures.html',
                  {'expenditures': expenditures, 'sum': sum, 'sum_month': sum_month, 'sum_week': sum_week})


def manage_incomes(request):
    if request.method == "POST":
        sum_i = request.POST.get('sum_i')
        name_i = request.POST.get('name_i')
        date_i = request.POST.get('date_i')
        if None or "" not in [name_i, sum_i, date_i]:
            income = Income(sum=sum_i, date=date_i, name=name_i)
            income.save()

    incomes = Income.objects.order_by('-date')[:10]
    sum = Income.objects.aggregate(Sum('sum'))
    sum_month = Income.objects.filter(date__gte=dt.today() - timedelta(days=30)).aggregate(Sum('sum'))
    sum_week = Income.objects.filter(date__gte=dt.today() - timedelta(days=7)).aggregate(Sum('sum'))
    return render(request, 'manage_incomes.html',
                  {'incomes': incomes, 'sum': sum, 'sum_month': sum_month, 'sum_week': sum_week})


def see_all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'see_all_employees.html', {'employees': employees})


def fire_employee(request):
    if request.method == "POST":
        pesel_e = request.POST.get('pesel_e')
        Employee.objects.filter(pesel=pesel_e).delete()

    return render(request, 'fire_employee.html')


def promote_demote_employee(request):
    if request.method == "POST":
        pesel_e = request.POST.get('pesel_e')
        salary_e = request.POST.get('salary_e')
        if None and "" not in [salary_e, pesel_e]:
            promotion = Employee.objects.get(pesel=pesel_e)
            promotion.salary = salary_e
            promotion.save()

    return render(request, 'promote_demote_employee.html')


def see_all_incomes(request):
    incomes = Income.objects.all().order_by('-date')
    return render(request, 'see_all_incomes.html', {'incomes': incomes})


def see_all_expenditures(request):
    expenditures = Outcome.objects.all().order_by('-date')
    return render(request, 'see_all_expenditures.html', {'expenditures': expenditures})


def events(request):
    if request.method == "POST":
        name_e = request.POST.get('name_e')
        description_e = request.POST.get('description_e')
        time_e = request.POST.get('time_e')
        date_e = request.POST.get('date_e')

        if None and "" not in [name_e, time_e, date_e]:
            event = Event(name=name_e, description=description_e, time=time_e, date=date_e)
            event.save()

    date = dt.today()
    today = Event.objects.filter(date=dt.today(), time__gte=dt.now()).order_by('time')
    tomorrow = Event.objects.filter(date=dt.today() + timedelta(days=1)).order_by('time')
    next = Event.objects.filter(date=dt.today(), time__gte=dt.now()).order_by('time')[:1]

    return render(request, 'events.html', {'today': today, 'tomorrow': tomorrow, 'date': date, 'next': next})


def all_events(request):
    all = Event.objects.all().order_by('-date', '-time')
    return render(request, 'all_events.html', {'all': all})


def future_events(request):
    future = Event.objects.filter(date__gte=dt.today()).order_by('date', 'time')
    return render(request, 'future_events.html', {'future': future})


def credits(request):
    return render(request, 'credits.html')


def search_expenditures(request):
    if request.method == "POST":
        name = request.POST.get('name')
        date = request.POST.get('date')
        if name is not None and name != "":
            by_name = Outcome.objects.filter(name=name)
            return render(request, 'search_expenditures.html', {'to_view': by_name})
        elif date is not None and date != "":
            by_date = Outcome.objects.filter(date=date)
            return render(request, 'search_expenditures.html', {'to_view': by_date})
    return render(request, 'search_expenditures.html')


def search_incomes(request):
    if request.method == "POST":
        name = request.POST.get('name')
        date = request.POST.get('date')
        if name is not None and name != "":
            by_name = Income.objects.filter(name=name)
            return render(request, 'search_incomes.html', {'to_view': by_name})
        elif date is not None and date != "":
            by_date = Income.objects.filter(date=date)
            return render(request, 'search_incomes.html', {'to_view': by_date})
    return render(request, 'search_incomes.html')