import os

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


# MVT - Model View Template


def audio_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "audio")


class Artist(models.Model):
    class Status(models.IntegerChoices):
        UNVERIFIED = 0, 'unverified'
        VERIFIED = 1, 'verified'

    name = models.CharField(max_length=255)
    monthly_listeners = models.IntegerField(validators=[MinValueValidator(0)],
                                            default=0)
    slug = models.SlugField(unique=True)
    subscribers = models.IntegerField(validators=[MinValueValidator(0)],
                                      default=0)
    bio = models.TextField()
    verified = models.IntegerField(default=Status.UNVERIFIED, choices=Status)
    pfp = models.ImageField(default='default_image.jpg')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-monthly_listeners', 'name']

    def get_absolute_url(self):
        return '/artist/artist_' + str(self.pk)


class Release(models.Model):
    class Type(models.TextChoices):
        SINGLE = 'Single'
        EP = 'EP'
        ALBUM = 'Album'

    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE,
                               related_name='releases')

    def __str__(self):
        return f'{self.name} of {self.artist}'

    def get_absolute_url(self):
        return '/releases/release_' + str(self.pk)


class Song(models.Model):
    # id - автоматически определяется
    title = models.CharField(max_length=255)
    duration = models.IntegerField(validators=[MinValueValidator(1)])
    source = models.FilePathField(path=audio_path)
    release = models.ForeignKey(Release, on_delete=models.CASCADE,
                                related_name='songs')

    def __str__(self):
        return f'{self.title} from {self.release}'

    def get_absolute_url(self):
        return '/artist/artist_' + str(self.pk)
