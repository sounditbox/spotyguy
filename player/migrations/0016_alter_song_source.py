# Generated by Django 5.0.2 on 2024-06-11 15:19

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0015_rename_user_playlist_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='source',
            field=models.FilePathField(path=pathlib.PureWindowsPath('C:/Users/Admin/PycharmProjects/spotybig/spotyguy/media/audio')),
        ),
    ]
