# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20151104_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='due date'),
        ),
    ]
