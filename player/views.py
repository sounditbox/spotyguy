from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    context = {'title': 'Главная страница'}
    return render(request, 'index.html', context)