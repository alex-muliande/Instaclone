from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts=[
    {
        'user': 'Alex',
        'image': 'imagehttps://cdn.pixabay.com/photo/2019/09/04/02/52/road-4450611__340.jpg',
        'caption': 'things by me',
    },
    {
        'user': 'Alphy',
        'image': '........',
        'caption': 'things by us',
    }
]

# Create your views here.
def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'index.html',context)  