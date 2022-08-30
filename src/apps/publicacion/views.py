from django.shortcuts import render
from .models import post

# Create your views here.

def post_list(request):
    posts = post.objects.all()
    print(posts.query)
    return render(request, 'blog.html', {'posts': posts})