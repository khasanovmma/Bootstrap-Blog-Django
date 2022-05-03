from django.shortcuts import render


def login_form(request):
    return render(request, 'members/login_form.html')

def register_form(request):
    return render(request, 'members/register_form.html')
