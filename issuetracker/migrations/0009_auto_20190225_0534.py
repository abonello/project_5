# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-25 05:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0008_auto_20190225_0511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='user',
        ),
        migrations.RemoveField(
            model_name='issuecomment',
            name='user',
        ),
    ]
