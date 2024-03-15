from django.urls import path
from .views import index, artist
urlpatterns = [
    path('', index, name='index'),
    path('artist/<slug:artist_slug>', artist, name='artist'),
]