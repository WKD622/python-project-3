from django.conf.urls import url
from howdy import views

# to są moje urle
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_to_database\.html', views.add_to_database),
    url(r'^manage_employees\.html', views.manage_employees),
    url(r'^manage_incomes\.html', views.manage_incomes),
    url(r'^manage_expenditures\.html', views.manage_expenditures)
]
