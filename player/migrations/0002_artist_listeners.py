# Generated by Django 5.0.1 on 2024-01-31 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="artist",
            name="listeners",
            field=models.IntegerField(
                default=0, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
