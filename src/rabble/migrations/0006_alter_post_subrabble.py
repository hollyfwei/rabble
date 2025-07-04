# Generated by Django 5.1.7 on 2025-04-21 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rabble", "0005_alter_subrabble_identifier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="subrabble",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="rabble.subrabble",
            ),
        ),
    ]
