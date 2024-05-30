# Generated by Django 5.0.2 on 2024-05-30 17:22

import django.core.validators
import django.db.models.deletion
import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0012_release_cover_release_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Playlist",
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
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "cover",
                    models.ImageField(
                        default="default__cover_image.jpg",
                        null=True,
                        upload_to="",
                        verbose_name="Обложка",
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="artist",
            options={
                "ordering": ["-monthly_listeners", "name"],
                "verbose_name": "Артист",
                "verbose_name_plural": "Артисты",
            },
        ),
        migrations.AlterField(
            model_name="artist",
            name="bio",
            field=models.TextField(verbose_name="Био"),
        ),
        migrations.AlterField(
            model_name="artist",
            name="monthly_listeners",
            field=models.IntegerField(
                default=0,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Слушатели",
            ),
        ),
        migrations.AlterField(
            model_name="artist",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="artist",
            name="pfp",
            field=models.ImageField(
                default="default_image.jpg", upload_to="", verbose_name="Аватарка"
            ),
        ),
        migrations.AlterField(
            model_name="artist",
            name="slug",
            field=models.SlugField(unique=True, verbose_name="Слаг"),
        ),
        migrations.AlterField(
            model_name="artist",
            name="verified",
            field=models.IntegerField(
                choices=[(0, "unverified"), (1, "verified")],
                default=0,
                verbose_name="Верификация",
            ),
        ),
        migrations.AlterField(
            model_name="release",
            name="artist",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="releases",
                to="player.artist",
                verbose_name="Исполнитель",
            ),
        ),
        migrations.AlterField(
            model_name="release",
            name="cover",
            field=models.ImageField(
                default="default__cover_image.jpg",
                null=True,
                upload_to="",
                verbose_name="Обложка",
            ),
        ),
        migrations.AlterField(
            model_name="release",
            name="date",
            field=models.DateField(auto_now_add=True, verbose_name="Дата выпуска"),
        ),
        migrations.AlterField(
            model_name="release",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="release",
            name="type",
            field=models.CharField(
                choices=[("Single", "Single"), ("EP", "Ep"), ("Album", "Album")],
                default="Single",
                max_length=50,
                verbose_name="Тип",
            ),
        ),
        migrations.AlterField(
            model_name="song",
            name="duration",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Длительность",
            ),
        ),
        migrations.AlterField(
            model_name="song",
            name="release",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="songs",
                to="player.release",
                verbose_name="Релиз",
            ),
        ),
        migrations.AlterField(
            model_name="song",
            name="source",
            field=models.FilePathField(
                path=pathlib.PureWindowsPath(
                    "D:/_/work/DjangoProject/spotiguy/media/audio"
                )
            ),
        ),
        migrations.AlterField(
            model_name="song",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Название"),
        ),
        migrations.CreateModel(
            name="SongInPlaylist",
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
                ("date_added", models.DateField(auto_now=True)),
                (
                    "playlist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="songs",
                        to="player.playlist",
                    ),
                ),
                (
                    "song",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="player.song"
                    ),
                ),
            ],
        ),
    ]
