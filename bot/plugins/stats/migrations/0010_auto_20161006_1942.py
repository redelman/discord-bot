# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0009_remove_gamesession__game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesession',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
    ]