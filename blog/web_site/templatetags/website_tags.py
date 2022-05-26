from django import template
from .models import Profile

register = template.Library()


@register.simple_tag
def current_time(request):
    user_page = Profile.objects.get(user=request.user)
    return {'user_page': user_page}