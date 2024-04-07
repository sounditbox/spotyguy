from django.urls import path
from .views import index, artist, release

urlpatterns = [
    path('', index, name='index'),
    path('artist/<slug:artist_slug>', artist, name='artist'),
    path('release/<int:release_id>', release, name='release'),
]
