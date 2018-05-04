# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photo.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photo.Location'),
            preserve_default=False,
        ),
    ]