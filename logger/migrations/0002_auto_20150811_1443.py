# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runinfo',
            name='starttime0',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 12, 43, 31, 283581, tzinfo=utc), verbose_name=b'Run start time '),
        ),
    ]
