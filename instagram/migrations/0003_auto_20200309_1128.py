# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-09 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20200308_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile'),
        ),
    ]