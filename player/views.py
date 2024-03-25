from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Artist


def index(request: HttpRequest):
    context = {'artists': Artist.objects.all(), 'some_list': [1, 2, 3, 4, 5, 6, 7], 'some_value': 4}
    return render(request, 'index.html', context)


def artist(request: HttpRequest, artist_slug):
    a = get_object_or_404(Artist, slug=artist_slug)
    context = {
        'status': Artist.Status(a.VERIFIED).label,
        'artist': a
    }
    return render(request, 'artist.html', context)


def template_tags_and_filters_example(request: HttpRequest):
    return render(request, 'template_example.html')