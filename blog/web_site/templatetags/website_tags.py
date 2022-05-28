from django import template
from web_site.models import Profile, Post

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