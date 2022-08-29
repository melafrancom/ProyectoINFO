from django.shortcuts import render
from django.contrib.auth.models import User
#from django.urls import reverse_lazy

def index(request):
    template_name = "index.html"
    ctx = {}
    return render(request, template_name, ctx)


def objetivos(request):
    template_name = "objetivos.html"
    ctx = {}
    return render(request, template_name, ctx)