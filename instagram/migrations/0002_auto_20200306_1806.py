# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-06 18:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='likes',
            new_name='like',
        ),
    ]