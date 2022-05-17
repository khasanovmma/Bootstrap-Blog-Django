from re import template
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from web_site.models import Profile
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView, ListView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import SignUpForm, EditAccountForm, ChangePasswordForm, ResetPasswordForm, SetNewPasswordForm

class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = 'Registration was successfully completed'
    
class UserEditAccountView(SuccessMessageMixin, UpdateView):
    form_class = EditAccountForm
    template_name = 'registration/edit_account.html'
    success_url = reverse_lazy('edit_account')
    success_message = 'Account data successfully updated '

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
        print(self.kwargs['username'])
        user = User.objects.get(username=self.kwargs['username'])
        print(user.pk)
        user_profile = get_object_or_404(Profile, user=user.pk)
        context = super().get_context_data(**kwargs)
        context["user_page"] =  user_profile
        return context
    
    
   