# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0003_auto_20161113_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='entry_type',
        ),
    ]