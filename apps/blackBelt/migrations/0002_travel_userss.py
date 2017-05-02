# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg', '0002_auto_20170324_0940'),
        ('blackBelt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='userss',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users_on_trip', to='loginReg.User'),
            preserve_default=False,
        ),
    ]
