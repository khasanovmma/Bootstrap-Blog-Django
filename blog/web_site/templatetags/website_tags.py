from django import template
from web_site.models import Profile, Post, Comment, Category
from django.db.models import Count

register = template.Library()


@register.simple_tag()
def user_profile(request):
    user_page = Profile.objects.get(user=request.user)
    return user_page

@register.simple_tag()
def user_profile_image(user_pk):
    profile = Profile.objects.get(user=user_pk)
    return profile.image_url
    
@register.simple_tag()
def get_latest_post():
    posts = Post.objects.all().order_by('-id')[:3]
    return posts

@register.simple_tag()
def post_data(request, post_id):
    post = Post.objects.get(pk=post_id)
    comment = Comment.objects.filter(post=post_id)
    context = {
        'liked': post.like_from_user(request),
        'total_comment': comment.count(),
        'total_views': post.views_count()
    }
    return context

@register.simple_tag()
def get_post_by_like(request):
    posts = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')
    data_list = []
    for post in posts: 
        liked =  Post.objects.get(pk=post.pk).like_from_user(request)
        data_list.append({'post': post, 'liked': liked})
    return data_list

@register.simple_tag()
def get_category():
    category = Category.objects.all()
    return category

