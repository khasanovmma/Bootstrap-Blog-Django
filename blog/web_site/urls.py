from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', blog_page, name='blog'),
    path('post/', post_page, name='post'),
]