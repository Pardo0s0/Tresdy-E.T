from django.urls import path
from rest_producto import views
from rest_producto.viewlogin import logiin

urlpatterns = [
    path('lista_producto', views.lista_producto, name="lista_producto"),
    path('detalle_producto/<id>', views.detalle_producto, name="detalle_producto"),
    path('logiin',logiin,name='logiin')

]