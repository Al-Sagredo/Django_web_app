from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistroForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# FBV vista de registro
def registro_usuario(request):
    #si el usuario completa y envia el formulario
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()      # Guarda el usuario en la BD 
            login(request, usuario)    # Inicia sesión automáticamente
            return redirect('home')    # Redirige a la página principal
    #si llega a la pagina de registro (metodo GET)
    else: 
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form}) # sigue esta vía si el form.is_valid es false o si el metodo es GET


# CBV vista de home con mixin
class HomeView(LoginRequiredMixin, TemplateView):# Mixin: Solo los usuarios autenticados con una sesión válida pueden ver la página.
    template_name= 'home.html'