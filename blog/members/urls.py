from django.urls import path
from .views import *

urlpatterns = [
    path('login-form/', login_form, name='login_form'),
    path('register-form/', register_form, name='register_form'),
]
