# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0005_auto_20150814_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='runinfo',
            name='dia1supply',
            field=models.CharField(default=b'0', max_length=4, verbose_name=b'Diamond 1 HV supply ', choices=[(0, b'---'), (1, b'HV1'), (2, b'HV2'), (3, b'HV3'), (4, b'HV4'), (5, b'HV5'), (6, b'HV6'), (7, b'HV7'), (8, b'HV8')]),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='dia2supply',
            field=models.CharField(default=b'0', max_length=4, verbose_name=b'Diamond 2 HV supply ', choices=[(0, b'---'), (1, b'HV1'), (2, b'HV2'), (3, b'HV3'), (4, b'HV4'), (5, b'HV5'), (6, b'HV6'), (7, b'HV7'), (8, b'HV8')]),
        ),
    ]
