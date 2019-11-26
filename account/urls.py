from django.contrib import admin
from django.urls import path, include
from account import views

urlpatterns = [
    path("register/",views.register, name="register" ),
    # path("login/",views.loginpage, name="login" ),
    path("details/",views.login, name="detail" ),
    path("authenticate/",include('django.contrib.auth.urls')),
]









