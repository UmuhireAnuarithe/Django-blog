from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {"post_list":posts})