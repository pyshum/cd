# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basecloud', '0004_customersorder_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersorder',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customersorder',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customersorder',
            name='image',
            field=models.ImageField(height_field=b'height_field', width_field=b'sidth_field', null=True, upload_to=b'', blank=True),
        ),
    ]
