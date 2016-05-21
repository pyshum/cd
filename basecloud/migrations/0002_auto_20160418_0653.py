# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basecloud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomersOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('create_date', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('rate', models.IntegerField(default=0, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb9\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81')),
            ],
            options={
                'verbose_name': '\u0441\u0442\u0430\u0442\u0443\u0441\u044b',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0443\u0441',
            },
        ),
        migrations.RemoveField(
            model_name='signup',
            name='stl_file',
        ),
    ]
