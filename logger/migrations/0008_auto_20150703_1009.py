# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0007_auto_20150703_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runinfo',
            name='starttime',
        ),
        migrations.AddField(
            model_name='runinfo',
            name='starttime0',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 10, 9, 43, 33265, tzinfo=utc), verbose_name=b'Run start time '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='starttime1',
            field=models.TimeField(default=datetime.datetime(2015, 7, 3, 10, 9, 43, 33296, tzinfo=utc), verbose_name=b'Beam stopper opening time '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='starttime2',
            field=models.TimeField(default=datetime.datetime(2015, 7, 3, 10, 9, 43, 33317, tzinfo=utc), verbose_name=b'Beam stopper open '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='TLUrate',
            field=models.PositiveIntegerField(verbose_name=b'TLU rate [Hz] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='aimedflux',
            field=models.PositiveIntegerField(verbose_name=b'Aimed flux [kHz]'),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='comments',
            field=models.TextField(verbose_name=b'Comments ', blank=True),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia1hv',
            field=models.IntegerField(verbose_name=b'Diamond 1 high voltage [V] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia2hv',
            field=models.IntegerField(verbose_name=b'Diamond 2 high voltage [V] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='endtime',
            field=models.DateTimeField(default=0, verbose_name=b'Run stop time '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='fs11',
            field=models.IntegerField(verbose_name=b'FS11 setting [mm] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='fs13',
            field=models.IntegerField(verbose_name=b'FS13 setting [mm] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='maskfile',
            field=models.CharField(max_length=200, verbose_name=b'Mask file '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='measuredflux',
            field=models.PositiveIntegerField(verbose_name=b'Measured flux [kHz] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='prescaledrate',
            field=models.PositiveIntegerField(verbose_name=b'Prescaled rate [Hz] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='pulserrate',
            field=models.PositiveIntegerField(verbose_name=b'Pulser rate [Hz] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='quadrupole',
            field=models.IntegerField(verbose_name=b'Quadrupole setting [%] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='rawrate',
            field=models.PositiveIntegerField(verbose_name=b'Raw rate [Hz] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='runtype',
            field=models.CharField(max_length=10, verbose_name=b'Run type ', choices=[(b'test', b'test'), (b'signal', b'signal'), (b'pedestal', b'pedestal')]),
        ),
    ]
