from django.contrib import admin
from .models import Category, Post, Profile, Comment

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Category)
