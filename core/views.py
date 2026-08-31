from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistroForm

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()      # Guarda el usuario en la BD 
            login(request, usuario)    # Inicia sesión automáticamente
            return redirect('home')    # Redirige a la página principal
    else: # metodo GET
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form}) # sigue esta vía si el form.is_valid es false o si el metodo es GET
