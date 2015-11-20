# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import logger.models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0009_auto_20151102_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runinfo',
            name='dia1',
            field=models.CharField(default=logger.models.getPrevDiamond1, max_length=200, verbose_name=b'Diamond 1 ', choices=[(b'---', b'---'), (b'II6-B2', b'II6-B2'), (b'II6-94', b'II6-94'), (b'II6-95', b'II6-95'), (b'II6-96', b'II6-96'), (b'II6-97', b'II6-97'), (b'II6-A0', b'II6-A0'), (b'A', b'A'), (b'B', b'B'), (b'D', b'D'), (b'S129', b'S129'), (b'2A87-E', b'2A87-E'), (b'IIa-1', b'IIa-1'), (b'IIa-2', b'IIa-2'), (b'IIa-3', b'IIa-3'), (b'IIa-5', b'IIa-5'), (b'other', b'other')]),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia1supply',
            field=models.CharField(default=logger.models.getPrevHVSupply1, max_length=4, verbose_name=b'Diamond 1 HV supply ', choices=[(b'0', b'---'), (b'1', b'HV1'), (b'2', b'HV2'), (b'3', b'HV3'), (b'4', b'HV4'), (b'5', b'HV5'), (b'6', b'HV6'), (b'7-1', b'HV7-CH1'), (b'7-2', b'HV7-CH2'), (b'7-3', b'HV7-CH3'), (b'7-4', b'HV7-CH4'), (b'7-5', b'HV7-CH5'), (b'8', b'HV8')]),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia2',
            field=models.CharField(default=logger.models.getPrevDiamond2, max_length=200, verbose_name=b'Diamond 2 ', choices=[(b'---', b'---'), (b'II6-B2', b'II6-B2'), (b'II6-94', b'II6-94'), (b'II6-95', b'II6-95'), (b'II6-96', b'II6-96'), (b'II6-97', b'II6-97'), (b'II6-A0', b'II6-A0'), (b'A', b'A'), (b'B', b'B'), (b'D', b'D'), (b'S129', b'S129'), (b'2A87-E', b'2A87-E'), (b'IIa-1', b'IIa-1'), (b'IIa-2', b'IIa-2'), (b'IIa-3', b'IIa-3'), (b'IIa-5', b'IIa-5'), (b'other', b'other')]),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia2supply',
            field=models.CharField(default=logger.models.getPrevHVSupply2, max_length=4, verbose_name=b'Diamond 2 HV supply ', choices=[(b'0', b'---'), (b'1', b'HV1'), (b'2', b'HV2'), (b'3', b'HV3'), (b'4', b'HV4'), (b'5', b'HV5'), (b'6', b'HV6'), (b'7-1', b'HV7-CH1'), (b'7-2', b'HV7-CH2'), (b'7-3', b'HV7-CH3'), (b'7-4', b'HV7-CH4'), (b'7-5', b'HV7-CH5'), (b'8', b'HV8')]),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='runtype',
            field=models.CharField(default=logger.models.getPrevRunType, max_length=10, verbose_name=b'Run type ', choices=[(b'test', b'test'), (b'signal', b'signal'), (b'pedestal', b'pedestal'), (b'tlu_no_handshare', b'tlu no handshake'), (b'find_shadow', b'find shadow'), (b'rate_scan', b'rate scan')]),
        ),
    ]
