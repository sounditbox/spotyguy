import os

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


# MVT - Model View Template


def audio_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "audio")


class Artist(models.Model):
    class Status(models.IntegerChoices):
        unverified = 0, 'unverified'
        verified = 1, 'verified'

    name = models.CharField(max_length=255)
    monthly_listeners = models.IntegerField(validators=[MinValueValidator(0)],
                                            default=0)
    slug = models.SlugField(unique=True)
    subscribers = models.IntegerField(validators=[MinValueValidator(0)],
                                      default=0)
    bio = models.TextField()
    verified = models.IntegerField(default=Status.unverified, choices=Status)
    pfp = models.ImageField(default='default_image.jpg')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-monthly_listeners', 'name']

    def get_absolute_url(self):
        return '/artist/artist_' + str(self.pk)


class Song(models.Model):
    # id - автоматически определяется
    title = models.CharField(max_length=255)
    duration = models.IntegerField(validators=[MinValueValidator(1)])
    source = models.FilePathField(path=audio_path)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} of {self.artist}'

    def get_absolute_url(self):
        return '/artist/artist_' + str(self.pk)
