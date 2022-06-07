from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/<int:pk>/', PostListByCategory.as_view(), name='category'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add-post/', AddPostView.as_view(), name='add_post'),
    path('post/<int:pk>/add-comment/', AddCommentView.as_view(), name='add_comment'),
    path('like', LikeView.as_view(), name='like'),
    path('post/', post_page, name='post'),
]