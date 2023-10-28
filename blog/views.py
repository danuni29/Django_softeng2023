from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-updated_at')
    return render(
        request,
        'blog/index.html',
    {
        'posts': posts,
    }
    )

def single_post_page(request, pk):
    posts = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/single_post_page.html',
    {
        'posts': posts,
    }
    )
