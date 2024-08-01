from django.shortcuts import render

from users.forms import UserLoginForm

def login(request):
    form  = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html')

def registration(request):
    context = {
        'title': 'Регистрация',
    }
    return render(request, 'users/registration.html')

def profile(request):
    context = {
        'title': 'Профиль',
    }
    return render(request, 'users/profile.html')

def logout(request):
    ...