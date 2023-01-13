from django.shortcuts import render
from .models import Post
<<<<<<< HEAD

# Create your views here.
def index(request):
    posts = Post.objects.all()

    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts
        })

def single_post_page(request, value):
    post = Post.objects.get(pk=value)

    return render(
        request,
        'blog/single_post_page.html',
        {
        'post' : post,
        }
        )
=======
def index(request):
    posts =	Post.objects.all()
    return render(
        request,	
        'blog/index.html',
        {
            'posts': posts
        }
    )
>>>>>>> 4a42328b47e97d4012693f525441199a456f604b
