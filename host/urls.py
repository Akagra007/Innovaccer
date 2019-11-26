from django.contrib import admin
from django.urls import path, include
from host import views
urlpatterns = [
    path('',views.home,name="home")
]
