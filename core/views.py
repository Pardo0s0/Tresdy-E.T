from ast import If
from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.


def home(request):

    return render(request, 'core/home.html')


def perfil(request):
    return render(request, 'core/perfil.html',)

def producta(request):
    posts = Producto.objects.all()
    return render(request, 'core/producto.html',{"posts": posts})
    
def ejemplo(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, 'core/ejemplo.html', contexto)
 
def crearProducto(request):
    contexto = {'form': ProductoForm()}
    if request.method == "POST":
        producto = ProductoForm(request.POST)
        if producto.is_valid:
            producto.save()
    return render(request, 'core/crearVehiculo.html', contexto)

def modificarProducto(request, id):
    producto = Producto.objects.get(codigo=id) 
    datos = {'form': ProductoForm(instance=producto)}
    if request.method == "POST": 
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid:
            form.save()
            datos["form"] = form
    return render(request, 'core/crearVehiculo.html', datos)


def eliminarProducto(request, id):
    producto = Producto.objects.get(codigo=id)
    producto.delete()
    return redirect(to="home")
 

def registro(request):    
    if request.method == 'POST':
        form =RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    else: 
        form = RegistroForm()      
        return render(request, 'core/registro.html', {'form':form})