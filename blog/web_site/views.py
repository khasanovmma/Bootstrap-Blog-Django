from turtle import pos
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from requests import get
from .forms import PostForm, EditForm
from .models import Post, Category, Profile, Ip, Comment
import json
from django.http import HttpResponse
from .utils import get_client_ip
from django.contrib.auth.models import User

class HomePageView(ListView):
    model = Post
    template_name = 'web_site/index.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'web_site/post_details.html'
    

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        post_info = get_object_or_404(Post, id=self.kwargs['pk'])
        
        ip = get_client_ip(self.request)

        if Ip.objects.filter(ip=ip).exists():
            post_info.views.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(ip=ip)
            post_info.views.add(Ip.objects.get(ip=ip)) 

       
        total_like = post_info.total_likes()
        views_count = post_info.views_count()
        profile = Profile.objects.get(user=post_info.author) 
        liked = post_info.likes.filter(id=self.request.user.id).exists()
        comments = Comment.objects.filter(post=post_info)

        context["profile_image"] = profile.image_url
        context["total_like"] = total_like
        context["comments_count"] = comments.count()
        context["comments"] = comments
        context["views_count"] = views_count
        context["liked"] = liked
        return context
    
class LikeView(TemplateView):
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get("post_id")
        post = Post.objects.get(pk=post_id)
        liked = False

        if not post.likes.filter(id=request.user.id).exists():
            post.likes.add(request.user)
            liked = True
        else:
            post.likes.remove(request.user)
            liked = False
        print(post.likes.filter(id=request.user.id).exists())

        return HttpResponse(json.dumps({'liked': liked, 'total_likes': str(post.total_likes()), "post_id": post_id}), content_type='application/json')

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'web_site/add_post.html'

    def get_object(self):
        return User.objects.get(user=self.request.user)

def blog_page(request):
    return render(request, 'web_site/blog.html')

def post_page(request):
    return render(request, 'web_site/post.html')
