from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proyectos') # 1 usuario varios proyectos
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas') # 1 proyecto varias tareas
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas') # 1 usuario varias tareas
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'{self.nombre} ({self.proyecto.nombre})'
