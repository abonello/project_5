# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-09 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0009_auto_20190225_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
    ]
