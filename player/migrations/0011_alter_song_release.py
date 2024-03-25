# Generated by Django 5.0.2 on 2024-03-25 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0010_remove_song_artist_release_song_release"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="release",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="songs",
                to="player.release",
            ),
        ),
    ]
