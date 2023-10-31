
from django.shortcuts import render
from django.views.generic import ListView

from .models import Post
# Create your views here.

class PostList(ListView):
    model = Post
    ordering = "-pk"


# def index(request):
#     posts = Post.objects.all().order_by('-updated_at')
#     return render(
#         request,
#         'blog/post_list.html',
#     {
#         'posts': posts,
#     }
#     )

def single_post_page(request, pk):
    posts = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/single_post_page.html',
    {
        'posts': posts,
    }
    )
