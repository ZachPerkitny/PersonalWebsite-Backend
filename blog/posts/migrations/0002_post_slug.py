# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, editable=False, unique=True),
            preserve_default=False,
        ),
    ]
