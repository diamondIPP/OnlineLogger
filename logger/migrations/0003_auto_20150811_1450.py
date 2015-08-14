# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0002_auto_20150811_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runinfo',
            name='starttime0',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 12, 50, 28, 781380, tzinfo=utc), verbose_name=b'Run start time '),
        ),
    ]
