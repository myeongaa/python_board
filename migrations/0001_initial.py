# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-14 06:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2017, 7, 14, 15, 20, 12, 800879))),
            ],
        ),
    ]