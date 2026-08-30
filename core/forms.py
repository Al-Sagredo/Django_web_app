from django.contrib.auth.forms import UserCreationForm #formulario base para registrar usuarios
from django.contrib.auth.models import User #tabla usuario en BD
from django import forms

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required= False)
    class Meta(UserCreationForm.Meta): #UserCreationForm.Meta adjunta  los dos campos de contraseña.
        model = User
        fields = ['username', 'email']

