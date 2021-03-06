from django.forms import ModelForm
from .models import *


from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class RegistroForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields} 


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','nombre','categoria','stock','precio','descuento']