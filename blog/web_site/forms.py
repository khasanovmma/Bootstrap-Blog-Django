from logging import PlaceHolder
from django import forms
from .models import Post, Category, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'author','content',  'photo')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'author', 'type':'hidden'}),
            'category': forms.Select(choices=Category.objects.all(), attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'content',  'photo')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=Category.objects.all(), attrs={'class': 'form-control'}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type your comment'}),
        }
