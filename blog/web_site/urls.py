from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post-detail/<int:pk>', ArticleDetailView.as_view(), name='post_details'),
    path('add-post/', AddPostView.as_view(), name='add_post'),
    path('like', LikeView.as_view(), name='like'),
    path('blog/', blog_page, name='blog'),
    path('post/', post_page, name='post'),
]