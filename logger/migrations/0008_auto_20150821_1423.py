# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import logger.models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0007_auto_20150821_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runinfo',
            name='dia1supply',
            field=models.CharField(default=logger.models.getPrevHVSupply1, max_length=4, verbose_name=b'Diamond 1 HV supply ', choices=[(b'0', b'---'), (b'1', b'HV1'), (b'2', b'HV2'), (b'3', b'HV3'), (b'4', b'HV4'), (b'5', b'HV5'), (b'6', b'HV6'), (b'7', b'HV7'), (b'8', b'HV8')]),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia2supply',
            field=models.CharField(default=logger.models.getPrevHVSupply2, max_length=4, verbose_name=b'Diamond 2 HV supply ', choices=[(b'0', b'---'), (b'1', b'HV1'), (b'2', b'HV2'), (b'3', b'HV3'), (b'4', b'HV4'), (b'5', b'HV5'), (b'6', b'HV6'), (b'7', b'HV7'), (b'8', b'HV8')]),
        ),
    ]
