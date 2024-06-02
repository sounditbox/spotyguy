from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from .forms import LoginForm


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
