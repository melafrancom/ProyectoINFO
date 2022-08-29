from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    template_name = "index.html"
    ctx = {}
    return render(request, template_name, ctx)