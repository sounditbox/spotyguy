import os

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


# MVT - Model View Template


def audio_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "audio")


class Artist(models.Model):
    name = models.CharField(max_length=255)
    listeners = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.name


class Song(models.Model):
    # id - автоматически определяется
    title = models.CharField(max_length=255)
    duration = models.IntegerField(validators=[MinValueValidator(1)])
    source = models.FilePathField(path=audio_path)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
