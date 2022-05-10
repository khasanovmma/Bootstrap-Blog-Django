from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user =  models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    

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

