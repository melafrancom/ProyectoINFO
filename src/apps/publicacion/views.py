from email import message
from django.shortcuts import render, redirect, get_object_or_404
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
            form.save(commit=False)
            post.User = request.user
            messages.success(request, 'Post creado con éxito.')
            return redirect('post_list')
        message.error(request, 'Hay errores en el formulario!')
    return render(request, 'blog_create.html', {'form': form})

def post_update(request, pk):
    Post = get_object_or_404(post, id=pk)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, instance=Post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    return render(request, 'blog_update.html', {'form': form})