import os

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

from users.models import Profile


# MVT - Model View Template


def audio_path():
    return settings.AUDIO_PATH


class Artist(models.Model):
    class Status(models.IntegerChoices):
        UNVERIFIED = 0, 'unverified'
        VERIFIED = 1, 'verified'

    name = models.CharField(max_length=255, verbose_name='Имя')
    monthly_listeners = models.IntegerField(validators=[MinValueValidator(0)],
                                            default=0, verbose_name='Слушатели')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    subscribers = models.IntegerField(validators=[MinValueValidator(0)],
                                      default=0)
    bio = models.TextField(verbose_name='Био')
    verified = models.IntegerField(default=Status.UNVERIFIED, choices=Status, verbose_name='Верификация')
    pfp = models.ImageField(default='default_image.jpg', verbose_name='Аватарка')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-monthly_listeners', 'name']
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"

    def get_absolute_url(self):
        return '/artist/artist_' + str(self.pk)


class Release(models.Model):
    class Type(models.TextChoices):
        SINGLE = 'Single'
        EP = 'EP'
        ALBUM = 'Album'

    date = models.DateField(auto_now_add=True, verbose_name='Дата выпуска')
    name = models.CharField(max_length=255, verbose_name='Название')
    artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE,
                               related_name='releases', verbose_name='Исполнитель')
    type = models.CharField(default=Type.SINGLE, choices=Type, max_length=50, verbose_name='Тип')
    cover = models.ImageField(default='default__cover_image.jpg', null=True, verbose_name='Обложка')
    # add song
    def __str__(self):
        return f'{self.name} of {self.artist}'

    def get_absolute_url(self):
        return '/release/' + str(self.pk)


class Song(models.Model):
    # id - автоматически определяется
    title = models.CharField(max_length=255, verbose_name='Название')
    duration = models.IntegerField(validators=[MinValueValidator(1)], verbose_name='Длительность')
    source = models.FilePathField(path=settings.AUDIO_PATH)
    release = models.ForeignKey(Release, on_delete=models.CASCADE,
                                related_name='songs', verbose_name='Релиз')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/song/{self.pk}'

    def get_duration_formatted(self):
        # str.zfill(2)
        return f'{self.duration // 60}'.zfill(2) + ':' + f'{self.duration % 60}'.zfill(2)

    def get_relative_source(self):
        return self.source.split('\\')[-1]


class Playlist(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    cover = models.ImageField(default='default__cover_image.jpg', null=True, verbose_name='Обложка')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='playlists', null=True)

    # add public/private
    def __str__(self):
        return f'Playlist {self.name}'

    def get_absolute_url(self):
        return '/playlist/' + str(self.pk)


class SongInPlaylist(models.Model):
    song = models.ForeignKey(Song, on_delete=models.DO_NOTHING)
    playlist = models.ForeignKey(Playlist, on_delete=models.DO_NOTHING, related_name='songs')
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.song)

    def get_absolute_url(self):
        return '/song_in_playlist/' + str(self.pk)
