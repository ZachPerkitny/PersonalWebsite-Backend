# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 00:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20170828_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comments',
        ),
    ]