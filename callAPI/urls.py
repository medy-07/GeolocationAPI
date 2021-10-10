from django.urls import path

from . import views

urlpatterns = [
    path('getAddressDetails', views.getLatLong),
]