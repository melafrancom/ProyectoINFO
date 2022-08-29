from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, SignUpForm


# Create your views here.

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
                return redirect('principal')
            else:
                messages.info(request, 'Credenciles invalidas.')
        else:
            messages.error(request, 'Hay errores en el formulario.')
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('principal')


def regitrar_usuario(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST) #Aca cargamos el formulario con los datos del post
        if form.is_valid():
            new_user = form.save()
            print(new_user)
            messages.success(request, 'Usuario creado')
            return redirect('principal')
    return render(request, 'register.html', {'form': form})
