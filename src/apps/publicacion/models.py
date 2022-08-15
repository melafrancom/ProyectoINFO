from django.db import models

# Create your models here.

class post(models.Model):
    titulo = models.CharField("Titulo", max_length=250)



