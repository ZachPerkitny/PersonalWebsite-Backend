# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20170913_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='posts.Tag'),
        ),
    ]