# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20170926_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_type', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('stats', models.TextField()),
            ],
        ),
    ]
