from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Post

# def home_page(request):
#     return render(request, 'web_site/blog.html')

class HomePageView(ListView):
    model = Post
    template_name = 'web_site/index.html'
    

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def blog_page(request):
    return render(request, 'web_site/blog.html')

def post_page(request):
    return render(request, 'web_site/post.html')
