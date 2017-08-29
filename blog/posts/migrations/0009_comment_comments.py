# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 23:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.Comment'),
            preserve_default=False,
        ),
    ]
