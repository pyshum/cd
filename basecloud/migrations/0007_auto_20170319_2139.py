# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-19 18:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basecloud', '0006_auto_20170319_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customersprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
