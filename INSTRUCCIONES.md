# Tresdy-E.T
Examen transversal

--BASE DE DATOS--
  INSERTAR LA BASE DE DATOS EN SQL DEVELOPER



1 - actualizar visual (menú HELP->CHECK FOR UPDATES)

2 - descargar o abrir proyecto de ayer (base update en material extra)

3 - cambiar versión de python por una de 64 bits.

4 - matar la consola (icono tarro de basura) y reiniciar visual.

5 - instalar django, cx_oracle y crispy_forms

pip install django

pip install cx_oracle

pip install django-crispy-forms

pip install djangorestframework

6 - acceder a sqlplus y crear usuario (en duoc user system pass Duoc.2022)

create user django identified by django;

grant connect, resource to django;

alter user django default tablespace users quota unlimited on users;

7 - ejecutar migración.

python manage.py migrate

8 - crear superusuario.

python manage.py createsuperuser

9 - ejecutar proyecto, acceder al admin y crear 1 categoria y 1 producto

python manage.py runserver



---API---
/api/lista_vehiculo/1
/api/detalle_producto/1
/api/logiin
