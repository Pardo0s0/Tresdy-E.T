from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('crearProducto', crearProducto, name="crearProducto"),
    path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
    path('login', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path('ejemplo', ejemplo, name="ejemplo"),
    path('registro', registro, name="registro"),
    path('perfil', perfil, name="perfil"),
    path('producta', producta, name="producta"),
]
