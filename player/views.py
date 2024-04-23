from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Artist, Song
from .models import Release


def index(request: HttpRequest):
    context = {'artists': Artist.objects.all(),
               'some_list': [1, 2, 3, 4, 5, 6, 7], 'some_value': 4}
    return render(request, 'index.html', context)


def artist(request: HttpRequest, artist_slug):
    a = get_object_or_404(Artist, slug=artist_slug)
    context = {
        'status': Artist.Status(a.verified).label,
        'artist': a
    }
    return render(request, 'artist.html', context)


def release(request: HttpRequest, release_id):
    context = {"release": get_object_or_404(Release, id=release_id)}
    return render(request, 'release.html', context)


def song(request: HttpRequest, song_id):
    context = {'song': get_object_or_404(Song, id=song_id)}
    return render(request, 'song.html', context)


def template_tags_and_filters_example(request: HttpRequest):
    return render(request, 'template_example.html')
