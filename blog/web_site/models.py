from pyexpat import model
from django.db import models
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.CharField( max_length=100, default="Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
    profile_image = models.ImageField(upload_to='photo/profile', blank=True)
    phone = models.CharField(max_length=30,  default="+99871 1234567 (Default)", blank=True)
    mobile = models.CharField(max_length=30,  default="+99890 9999999 (Default)", blank=True)
    address = models.CharField(max_length=155,  default="Uzbekistan, Tashkent, Mirabad, Nukus street", blank=True)
    website_url = models.CharField(max_length=255,  default="#", blank=True)
    github_url = models.CharField(max_length=255,  default="#", blank=True)
    instagram_url = models.CharField(max_length=255,  default="#", blank=True)
    facebook_url = models.CharField(max_length=255,  default="#", blank=True)
    telegram_url = models.CharField(max_length=255,  default="#", blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"username": self.user.username})

    
    def image_url(self):
        try:
            url = self.profile_image.url
        except:
            url = 'https://cdn-icons-png.flaticon.com/512/711/711769.png'
            
        return url


class Category(models.Model):
    title = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse_lazy("category", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)
    views = models.ManyToManyField(Ip, related_name="post_views", blank=True)

    def total_likes(self):
        return self.likes.count()
    
    def views_count(self):
        return self.views.count()

    def __str__(self):
        return self.author.first_name
    
    def like_from_user(self, request):
        return self.likes.filter(id=request.user.id).exists()
    
    def photo_url(self):
        try:
            url = self.photo.url
        except:
            url = 'https://www.maisondalis.ma/wp-content/uploads/2022/02/image-coming-soon.jpg'
        return url

    def get_absolute_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.pk})
    
    


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    body = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title
    