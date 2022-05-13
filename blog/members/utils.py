from django.contrib.auth.models import User
from django.shortcuts import redirect
from social_core.exceptions import AuthException
from django.contrib import messages


def check_email_exists(request, backend, details, uid, user=None, *args, **kwargs):
    email = details.get('email', '')
    provider = backend.name

    # check if social user exists to allow logging in (not sure if this is necessary)
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    # check if given email is in use
    exists = User.objects.filter(email=email)

    # user is not logged in, social profile with given uid doesn't exist
    # and email is in use
    print(email)
    if len(exists) > 1 and email:
        messages.error(request,'Email exists')
        return redirect('login')
