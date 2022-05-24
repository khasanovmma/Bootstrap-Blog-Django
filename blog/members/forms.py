from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from web_site.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
       return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditAccountForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'

class SetNewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'

class EditProfileFrom(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'profile_image', 'phone', 'mobile', 'address', 'website_url', 'github_url', 'instagram_url', 'facebook_url', 'telegram_url')
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            # 'profile_image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}, ),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'telegram_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
    


  