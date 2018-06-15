from django.conf.urls import url
from howdy import views

# to są moje urle
urlpatterns = [
    url(r'^$', views.index),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
]
