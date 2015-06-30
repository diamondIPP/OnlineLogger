# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputMask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('persons', models.CharField(max_length=200, verbose_name=b'Persons on shift: ')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name=b'Date: ')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name=b'Time: ')),
            ],
        ),
    ]
