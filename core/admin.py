
from django.contrib import admin
from .models import Proyecto, Tarea

# Register your models here.

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

    list_filter= ('nombre',)
    
    search_fields = ('nombre',)

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

    list_filter= ('nombre',)
        
    search_fields = ('nombre',)





