# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0004_auto_20150630_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='runinfo',
            name='TLUrate',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TLU rate in Hz: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='aimedflux',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Aimed flux: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='dia1',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Diamond 1: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='dia1hv',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Diamond 1 high voltage: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='dia2',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Diamond 2: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='dia2hv',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Diamond 2 high voltage: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='fs11',
            field=models.IntegerField(default=0, verbose_name=b'FS11 setting: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='fs13',
            field=models.IntegerField(default=0, verbose_name=b'FS13 setting: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='maskfile',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Mask file: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='measuredflux',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Measured flux: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='prescaledrate',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Prescaled rate in Hz: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='pulserrate',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Pulser rate in Hz: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='quadrupole',
            field=models.IntegerField(default=100, verbose_name=b'Quadrupole setting in %: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='rawrate',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Raw rate in Hz: '),
        ),
    ]
