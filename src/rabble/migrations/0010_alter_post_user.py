# Generated by Django 5.1.7 on 2025-05-19 03:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rabble", "0009_alter_subrabble_visibility"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
