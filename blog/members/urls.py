from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_form, name='login_form'),
]
