# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basecloud', '0005_auto_20160516_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customersorder',
            name='image',
            field=models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=b'', blank=True),
        ),
    ]
