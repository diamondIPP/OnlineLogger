# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import logger.models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0006_auto_20150703_0720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runinfo',
            name='date',
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='TLUrate',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TLU rate [Hz] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='aimedflux',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Aimed flux [Hz]'),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='comments',
            field=models.TextField(default=b'', verbose_name=b'Comments '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia1',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Diamond 1 '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia1hv',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Diamond 1 high voltage [V] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia2',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Diamond 2 '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia2hv',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Diamond 2 high voltage [V] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='endtime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'End time '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='fs11',
            field=models.IntegerField(default=0, verbose_name=b'FS11 setting  '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='fs13',
            field=models.IntegerField(default=0, verbose_name=b'FS13 setting '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='maskfile',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Mask file '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='measuredflux',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Measured flux '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='persons',
            field=models.CharField(max_length=200, verbose_name=b'Persons on shift '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='prescaledrate',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Prescaled rate [Hz] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='pulserrate',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Pulser rate [Hz] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='quadrupole',
            field=models.IntegerField(default=100, verbose_name=b'Quadrupole setting [%] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='rawrate',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Raw rate [Hz] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='runnr',
            field=models.PositiveIntegerField(default=logger.models.getPrevRunNumber, verbose_name=b'Run number '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='starttime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Start time '),
        ),
    ]
