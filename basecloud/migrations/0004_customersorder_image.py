# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basecloud', '0003_signup_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersorder',
            name='image',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
