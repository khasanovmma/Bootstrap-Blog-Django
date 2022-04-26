from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', blog_page, name='blog'),
    path('post/', post_page, name='post'),
]