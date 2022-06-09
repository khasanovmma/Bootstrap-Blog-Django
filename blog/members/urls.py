from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit-account/', UserEditAccountView.as_view(), name="edit_account"),
    path('password/', UserChangePasswordtView.as_view(), name="password"),
    path('reset-password/', UserPasswordResetView.as_view(), name="reset_password"),
    path('profile/<str:username>', ShowProfilePageView.as_view(), name="profile"),
    path('edit-profile/', EditProfileView.as_view(), name="edit_profile"),
    path('reset/<uidb64>/<token>/', UserSetPasswordtView.as_view()),
    path('post/<int:pk>/eitd/', UpdatePostView.as_view(), name='update_post'),
]
