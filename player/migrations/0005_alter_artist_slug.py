# Generated by Django 5.0.2 on 2024-03-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0004_artist_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]