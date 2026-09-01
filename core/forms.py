from django.contrib.auth.forms import UserCreationForm #formulario base para registrar usuarios
from django.contrib.auth.models import User #tabla usuario en BD
from django import forms
from .models import Proyecto, Tarea

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required= False)
    class Meta(UserCreationForm.Meta): #UserCreationForm.Meta adjunta  los dos campos de contraseña.
        model = User
        fields = ['username', 'email']

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields= ['nombre', ]
        widgets ={
            'nombre':forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '')
        if len(nombre) <3:
            raise forms.ValidationError('El nombre del proyecto debe tener al menos 3 caracteres')
        return nombre

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre',]
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '')
        if len(nombre) <3:
            raise forms.ValidationError('El nombre de la tarea debe tener al menos 3 caracteres')
        return nombre