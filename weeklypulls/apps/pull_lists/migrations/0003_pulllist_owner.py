# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-09 02:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pull_lists', '0002_auto_20171224_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='pulllist',
            name='owner',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='snippets',
                to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
