# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0002_auto_20150630_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='runinfo',
            name='runnr',
            field=models.IntegerField(default=0, verbose_name=b'Run number: '),
        ),
    ]
