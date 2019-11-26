from django.contrib import admin
from django.urls import path, include
from visitors import views

urlpatterns = [
    path("checkin/",views.checkin, name="checkin" ),
    path("checkout/",views.checkout, name="checkout" ),
]