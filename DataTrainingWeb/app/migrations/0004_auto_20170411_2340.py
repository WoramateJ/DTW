# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 16:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170411_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='randomQueue',
            new_name='queue',
        ),
    ]