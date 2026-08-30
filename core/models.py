from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)


