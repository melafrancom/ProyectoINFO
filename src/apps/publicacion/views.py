from email import message
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import post
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = post.objects.all()
    print(posts.query)
    return render(request, 'blog.html', {'posts': posts})

def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.succes('Post creado con éxito.')
            return redirect('post_list')
        message.error(request, 'Hay errores en el formulario!')
    return render(request, 'blog_create.html')