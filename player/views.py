from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Artist


def index(request: HttpRequest):
    context = {'title': 'Главная страница'}
    return render(request, 'index.html', context)


def artist(request: HttpRequest, artist_slug):

    context = {
        'artist': get_object_or_404(Artist, slug=artist_slug)
    }
    return render(request, 'artist.html', context)
