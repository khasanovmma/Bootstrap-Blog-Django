from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Post

# def home_page(request):
#     return render(request, 'web_site/blog.html')

class HomePageView(ListView):
    model = Post
    template_name = 'web_site/index.html'

def blog_page(request):
    return render(request, 'web_site/blog.html')

def post_page(request):
    return render(request, 'web_site/post.html')
