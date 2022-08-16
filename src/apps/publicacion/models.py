from distutils.command.upload import upload
from django.db import models
from apps.accounts.models import User
from django.utils import timezone

# Create your models here.

class post(models.Model):
    titulo = models.CharField("Titulo", max_length=250)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='img/publicacion', help_text='Seleccione una imagen para mostrar:')
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateField(auto_now=True)
    publicado = models.DateField(blank=True, null=True)
    categorias = models.ManyToManyField('Categoria', related_name='publicacion')


class Coment(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    contenido = models.TextField("Contenido")
    creado = models.DateTimeField(default=timezone.now)


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)


