# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 06:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20170717_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 17, 15, 21, 20, 195435)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 17, 15, 21, 20, 195934)),
        ),
    ]