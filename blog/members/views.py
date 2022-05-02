from django.shortcuts import render


def login_form(request):
    return render(request, 'members/login_form.html')
