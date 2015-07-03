# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0005_auto_20150630_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runinfo',
            name='time',
        ),
        migrations.AddField(
            model_name='runinfo',
            name='endtime',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name=b'End time: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='starttime',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name=b'Start time: '),
        ),
    ]
