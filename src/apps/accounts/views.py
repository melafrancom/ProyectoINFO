from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm


# Create your views here.


def cuentas(request):
    
    template_name = "PruebaDeCuentas.html"
    ctx = {}
    return render(request, template_name, ctx)


def login_view(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(type(request.POST))
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                return redirect('')
            else:
                messages.info(request, 'Credenciles invalidas.')
        else:
            messages.error(request, 'Hay errores en el formulario.')
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('')