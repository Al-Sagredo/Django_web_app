
from django.contrib import admin
from .models import Proyecto, Tarea

# Register your models here.

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'fecha_creacion')

    list_filter= ('nombre', 'usuario')
    
    search_fields = ('nombre', 'usuario__username')

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'proyecto', 'usuario', 'fecha_creacion', 'completada')

    list_filter= ('proyecto', 'usuario', 'fecha_creacion', 'completada')
        
    search_fields = ('nombre', 'proyecto__nombre', 'usuario__username')





