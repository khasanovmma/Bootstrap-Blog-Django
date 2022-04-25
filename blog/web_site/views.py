from django.shortcuts import render, HttpResponse
from .models import Post

def home_page(request):

    return render(request, 'web_site/index.html')


def blog_page(request):
    context = {
        'main': 'О нас',
        'content': 'Страница о нас'
    }
    return render(request, 'web_site/blog.html')
