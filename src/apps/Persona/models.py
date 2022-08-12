from django.db import models
from django.utils import timezone


# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    class Meta:
        db_table = 'Personas'

"""
class Administrador(models.Model):
    id_persona = models.ForeignKey('auth.user')
    nombre_usuario = models.CharField(max_length=250)

class Visitante(models.Model):
    id_persona = models.ForeignKey('auth.user')
    nombre_usuario = models.CharField(max_length=250)

class Publicacion(models.Model):
    Id_Administrador = models.ForeignKey('auth.user')
    Id_Areas = models.ForeignKey('')
    Titulo = models.CharField(max_length=355)
    contenido = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='', help_text = "Seleccione una imagen para mostrar.")
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    publicado = models.DateField(blank=True, null=True)

class Areas(models.Model):
    tipo = models.CharField(max_length=200)

class Interaccion(models.Model):
    compartir = models.CharField(100)
"""





