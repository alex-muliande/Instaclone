from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    context ={
        'posts': posts
    }
    return render(request, 'index.html',context)  


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
