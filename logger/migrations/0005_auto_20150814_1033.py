# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import logger.models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0004_auto_20150812_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='runinfo',
            name='accepted_pulserrate',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Accepted pulser rate [Hz] '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='runinfo',
            name='for1',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Fast OR 1 [Hz] '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='runinfo',
            name='for2',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Fast OR 2 [Hz] '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='runinfo',
            name='tlu_input_rate',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TLU input rate [Hz] '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia1hv',
            field=models.FloatField(default=logger.models.getPrevVoltage1, verbose_name=b'Diamond 1 high voltage [V] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia2hv',
            field=models.FloatField(default=logger.models.getPrevVoltage2, verbose_name=b'Diamond 2 high voltage [V] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='fs11',
            field=models.FloatField(verbose_name=b'FS11 setting [steps] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='fs13',
            field=models.FloatField(verbose_name=b'FS13 setting [steps] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='maskfile',
            field=models.CharField(default=logger.models.getPrevMaskFile, max_length=200, verbose_name=b'Mask file '),
        ),
    ]
