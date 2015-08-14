# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import logger.models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0003_auto_20150811_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runinfo',
            name='TLUrate',
        ),
        migrations.RemoveField(
            model_name='runinfo',
            name='aimedflux',
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia1',
            field=models.CharField(default=logger.models.getPrevDiamond1, max_length=200, verbose_name=b'Diamond 1 ', choices=[(b'---', b'---'), (b'II6-B2', b'II6-B2'), (b'II6-94', b'II6-94'), (b'II6-95', b'II6-95'), (b'II6-96', b'II6-96'), (b'II6-97', b'II6-97'), (b'II6-A0', b'II6-A0'), (b'A', b'A'), (b'B', b'B'), (b'D', b'D'), (b'S129', b'S129'), (b'other', b'other')]),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia1hv',
            field=models.FloatField(verbose_name=b'Diamond 1 high voltage [V] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia2',
            field=models.CharField(default=logger.models.getPrevDiamond2, max_length=200, verbose_name=b'Diamond 2 ', choices=[(b'---', b'---'), (b'II6-B2', b'II6-B2'), (b'II6-94', b'II6-94'), (b'II6-95', b'II6-95'), (b'II6-96', b'II6-96'), (b'II6-97', b'II6-97'), (b'II6-A0', b'II6-A0'), (b'A', b'A'), (b'B', b'B'), (b'D', b'D'), (b'S129', b'S129'), (b'other', b'other')]),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia2hv',
            field=models.FloatField(verbose_name=b'Diamond 2 high voltage [V] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='fs11',
            field=models.FloatField(verbose_name=b'FS11 setting [mm] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='fs13',
            field=models.FloatField(verbose_name=b'FS13 setting [mm] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='measuredflux',
            field=models.FloatField(verbose_name=b'Measured flux [kHz/sqcm] '),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='runtype',
            field=models.CharField(max_length=10, verbose_name=b'Run type ', choices=[(b'test', b'test'), (b'signal', b'signal'), (b'pedestal', b'pedestal'), (b'tlu_no_handshare', b'tlu no handshake'), (b'find_shadow', b'find shadow'), (b'rate_scan', b'rate scan')]),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='starttime0',
            field=models.DateTimeField(default=datetime.timedelta(0), verbose_name=b'Run start time '),
        ),
    ]
