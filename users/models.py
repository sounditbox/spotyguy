from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    pfp = models.ImageField(default='default_image.jpg', verbose_name='Аватарка')
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
