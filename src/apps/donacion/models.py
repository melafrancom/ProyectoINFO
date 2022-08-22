from django.db import models
from apps.accounts.models import User
from django.utils import timezone


# Create your models here.
class donacion(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    realizado = models.DateTimeField(default=timezone.now)
