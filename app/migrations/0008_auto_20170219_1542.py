# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-19 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_syncdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='definition_rates',
            field=models.TextField(default='{}'),
        ),
        migrations.AddField(
            model_name='entry',
            name='phrases',
            field=models.TextField(default='[]'),
        ),
    ]
