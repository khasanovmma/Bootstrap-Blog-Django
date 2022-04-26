from django.shortcuts import render, HttpResponse
from .models import Post

def home_page(request):
    return render(request, 'web_site/blog.html')

def blog_page(request):
    return render(request, 'web_site/blog.html')

def post_page(request):
    return render(request, 'web_site/post.html')
