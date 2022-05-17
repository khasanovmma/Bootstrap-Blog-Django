from django.db import models
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user =  models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, default="Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
    profile_image = models.ImageField(upload_to='photo/profile', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=155, blank=True)
    website_url = models.CharField(max_length=255, blank=True)
    github_url = models.CharField(max_length=255, blank=True)
    instagram_url = models.CharField(max_length=255, blank=True)
    facebook_url = models.CharField(max_length=255, blank=True)
    telegram_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"username": self.user.username})
    

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



