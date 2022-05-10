from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit-account/', UserEditAccountView.as_view(), name="edit_account"),
    path('password/', UserChangePasswordtView.as_view(), name="password"),
    path('reset-password/', UserPasswordResetView.as_view(), name="reset_password"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('reset/<uidb64>/<token>/', UserSetPasswordtView.as_view()),
]
