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


def Nosotros(request):
    template_name = "nosotros.html"
    ctx = {}
    return render(request, template_name, ctx)


def Areas(request):
    template_name = "areas.html"
    ctx = {}
    return render(request, template_name, ctx)

def Blog(request):
    template_name = "blog.html"
    ctx = {}
    return render(request, template_name, ctx)