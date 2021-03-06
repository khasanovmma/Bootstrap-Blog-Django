from re import template
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from web_site.models import Profile, Post
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView, ListView, DeleteView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm, EditAccountForm, ChangePasswordForm, ResetPasswordForm, SetNewPasswordForm, EditProfileFrom, EditPostForm


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Registration was successfully completed'
    
class UserEditAccountView(SuccessMessageMixin, UpdateView):
    form_class = EditAccountForm
    template_name = 'registration/edit_account.html'
    success_url = reverse_lazy('edit_account')
    success_message = 'Account data successfully updated'

    def get_object(self):
        return self.request.user
    
class UserChangePasswordtView(SuccessMessageMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('edit_account')
    success_message = 'Password changed successfully'
    
class UserPasswordResetView(SuccessMessageMixin, PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'registration/reset_password_email.html'
    success_url = reverse_lazy('login')
    success_message = 'Check your email'
    
    
class UserSetPasswordtView(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = 'registration/reset_password_confirm.html'
    form_class = SetNewPasswordForm
    success_url = reverse_lazy('login')
    success_message = 'Password reset request completed successfully'
    
class ShowProfilePageView(ListView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs['username'])
        user_profile, created = Profile.objects.get_or_create(user=user)
        user_posts = Post.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context["user_page"] =  user_profile
        context["user_posts"] = user_posts
        return context

class EditProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = EditProfileFrom
    model= Profile
    template_name = 'registration/edit_profile.html'
    success_message = 'Profile data successfully updated'
    redirect_field_name = 'redirect_to'
    permission_required = ''
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse_lazy('profile', kwargs = {'username': self.request.user.username })

    def get_object(self):
        return get_object_or_404(self.model, user=self.request.user)
    

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'registration/update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'registration/delete.html'
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs = {'username': self.request.user.username })

   