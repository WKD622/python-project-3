from django.conf.urls import url
from manager import views

# to są moje urle
urlpatterns = [
    url(r'^$', views.index),
    url(r'^manage_employees\.html', views.manage_employees),
    url(r'^manage_incomes\.html', views.manage_incomes),
    url(r'^manage_expenditures\.html', views.manage_expenditures),
    url(r'^see_all_employees\.html', views.see_all_employees),
    url(r'^fire_employee\.html', views.fire_employee),
    url(r'^promote_demote_employee\.html', views.promote_demote_employee),
    url(r'^see_all_incomes\.html', views.see_all_incomes),
    url(r'^see_all_expenditures\.html', views.see_all_expenditures),
    url(r'^events.html', views.events),
    url(r'^all_events\.html', views.all_events),
    url(r'^future_events\.html', views.future_events),
    url(r'^credits\.html', views.credits),
    url(r'^search_expenditures\.html', views.search_expenditures),
    url(r'^search_incomes\.html', views.search_incomes)
]
