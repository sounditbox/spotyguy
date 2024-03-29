# Generated by Django 5.0.2 on 2024-03-25 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0009_alter_artist_pfp"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="song",
            name="artist",
        ),
        migrations.CreateModel(
            name="Release",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="releases",
                        to="player.artist",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="song",
            name="release",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="songs",
                to="player.release",
            ),
        ),
    ]
