from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, ProyectoForm, TareaForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Proyecto, Tarea

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



@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False) #pausar el guardado en la base de datos
            proyecto.usuario = request.user #Asigna manualmente la clave foránea del proyecto vinculándolo al usuario que tiene la sesión iniciada en ese momento
            proyecto.save() # insert
            return redirect('proyecto_detalle', pk= proyecto.pk)
    else: # (GET)
        form = ProyectoForm()
    return render(request, 'core/proyecto_form.html', {'form': form})

@login_required 
def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)# Obtener el registro de la base de datos
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.proyecto = proyecto
            tarea.usuario = request.user
            tarea.save()
            return redirect('proyecto_detalle', pk=proyecto.pk)
    else:
        form = TareaForm()
    return render(request, 'core/proyecto_detalle.html', {'proyecto': proyecto, 'form': form})

@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.filter(usuario=request.user)
    return render(request, 'core/proyecto_list.html', {'proyectos': proyectos})

@login_required
def alternar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.completada = not tarea.completada  # Invierte el booleano
        tarea.save()
    return redirect('proyecto_detalle', pk=tarea.proyecto.pk)

@login_required
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    proyecto_pk = tarea.proyecto.pk  # Guardamos la PK antes de borrar
    if request.method == 'POST':
        tarea.delete()
    return redirect('proyecto_detalle', pk=proyecto_pk)

@login_required
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyecto_detalle', pk=proyecto.pk)
    else:
        form = ProyectoForm(instance=proyecto)
        
    return render(request, 'core/proyecto_editar.html', {
        'form': form,
        'proyecto': proyecto
    })

@login_required
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
        
    return render(request, 'core/proyecto_confirmar_eliminar.html', {
        'proyecto': proyecto
    })

