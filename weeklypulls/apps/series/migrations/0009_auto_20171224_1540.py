# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-24 15:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0008_auto_20171224_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='idu',
            new_name='id',
        ),
    ]
