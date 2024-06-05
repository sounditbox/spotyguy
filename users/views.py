from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm


# Create your views here.


def login(request: HttpRequest):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponse('Log out')


def register(request: HttpRequest):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    return render(request, 'register.html', context={'form': form})
