from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.conf import settings
from apps.accounts.models import User



# Create your models here.

class post(models.Model):
    titulo = models.CharField("Titulo", max_length=250)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    contenido = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='img/publicacion', help_text='Seleccione una imagen para mostrar:')
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateField(auto_now=True)
    publicado = models.DateField(blank=True, null=True)
    #categorias = models.ManyToManyField('Categoria', related_name='publicacion')
    #slug = models.SlugField()

    def __str__(self):
        return self.titulo


class Coment(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coments')
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name='coments')
    contenido = models.TextField("Contenido")
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateField(auto_now=True)

    def __str__(self):
        return self.contenido[:10]


class Categoria(models.Model):
    nombre = models.CharField('Categoria', max_length=200)
    creado = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombre




