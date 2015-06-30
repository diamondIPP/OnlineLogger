# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0003_runinfo_runnr'),
    ]

    operations = [
        migrations.AddField(
            model_name='runinfo',
            name='comments',
            field=models.TextField(default=b'', verbose_name=b'Comments: '),
        ),
        migrations.AddField(
            model_name='runinfo',
            name='runtype',
            field=models.CharField(default=b'test', max_length=10, choices=[(b'test', b'test'), (b'signal', b'signal'), (b'pedestal', b'pedestal')]),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='runnr',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Run number: '),
        ),
    ]
