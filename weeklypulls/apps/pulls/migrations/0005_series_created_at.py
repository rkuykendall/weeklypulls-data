# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-11 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pulls', '0004_auto_20171010_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='pull',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
