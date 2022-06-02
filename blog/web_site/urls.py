from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/<int:pk>/', PostListByCategory.as_view(), name='category'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('add-post/', AddPostView.as_view(), name='add_post'),
    path('like', LikeView.as_view(), name='like'),
    path('blog/', blog_page, name='blog'),
    path('post/', post_page, name='post'),
]