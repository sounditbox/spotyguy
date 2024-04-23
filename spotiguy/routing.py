from django.urls import path

from .consumers import AudioPlayerConsumer

websocket_urlpatterns = [
    path('ws/audio_player/', AudioPlayerConsumer.as_asgi()),
]

