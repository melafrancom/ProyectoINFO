from django.contrib import admin

from .apps import PublicacionConfig
from .models import Categoria, Coment, post

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Coment)
admin.site.register(post)

