# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import logger.models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0008_auto_20150703_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runinfo',
            name='persons',
            field=models.CharField(default=logger.models.getPrevPersons, max_length=200, verbose_name=b'Persons on shift '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='starttime0',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 11, 34, 10, 135425, tzinfo=utc), verbose_name=b'Run start time '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='starttime1',
            field=models.TimeField(default=datetime.timedelta(0), verbose_name=b'Beam stopper opening time ', blank=True),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='starttime2',
            field=models.TimeField(default=datetime.timedelta(0), verbose_name=b'Beam stopper open ', blank=True),
        ),
    ]
