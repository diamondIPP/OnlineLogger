# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import logger.models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0008_auto_20150821_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runinfo',
            name='quadrupole',
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia1',
            field=models.CharField(default=logger.models.getPrevDiamond1, max_length=200, verbose_name=b'Diamond 1 ', choices=[(b'---', b'---'), (b'II6-B2', b'II6-B2'), (b'II6-94', b'II6-94'), (b'II6-95', b'II6-95'), (b'II6-96', b'II6-96'), (b'II6-97', b'II6-97'), (b'II6-A0', b'II6-A0'), (b'A', b'A'), (b'B', b'B'), (b'D', b'D'), (b'S129', b'S129'), (b'2A87-E', b'2A87-E'), (b'other', b'other')]),
        ),
        migrations.AlterField(
            model_name='runinfo',
            name='dia2',
            field=models.CharField(default=logger.models.getPrevDiamond2, max_length=200, verbose_name=b'Diamond 2 ', choices=[(b'---', b'---'), (b'II6-B2', b'II6-B2'), (b'II6-94', b'II6-94'), (b'II6-95', b'II6-95'), (b'II6-96', b'II6-96'), (b'II6-97', b'II6-97'), (b'II6-A0', b'II6-A0'), (b'A', b'A'), (b'B', b'B'), (b'D', b'D'), (b'S129', b'S129'), (b'2A87-E', b'2A87-E'), (b'other', b'other')]),
        ),
    ]
