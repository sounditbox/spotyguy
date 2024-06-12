from django.urls import path
from .views import index, artist, release, song, playlist, player

urlpatterns = [
    path('', index, name='index'),
    path('artist/<slug:artist_slug>', artist, name='artist'),
    path('release/<int:release_id>', release, name='release'),
    path('playlist/<int:pl_id>', playlist, name='playlist'),
    path('song/<int:song_id>', song, name='song'),
    path('player/', player, name='player')
]
