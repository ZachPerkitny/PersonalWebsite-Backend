# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 00:10
from __future__ import unicode_literals

from django.db import migrations, models
from django.template.defaultfilters import slugify
from blog.posts.models import Tag


def migrate_data_forward(apps, schema_editor):
    for instance in Tag.objects.all():
        instance.tag = slugify(instance.word)
        instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_auto_20170913_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(null=True, default=None, editable=False, unique=True),
            preserve_default=False,
        ),
        migrations.RunPython(
          migrate_data_forward,
        ),
    ]