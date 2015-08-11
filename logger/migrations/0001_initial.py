# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import logger.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RunInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('persons', models.CharField(default=logger.models.getPrevPersons, max_length=200, verbose_name=b'Persons on shift ')),
                ('runnr', models.PositiveIntegerField(default=logger.models.getPrevRunNumber, verbose_name=b'Run number ')),
                ('starttime0', models.DateTimeField(default=datetime.datetime(2015, 8, 11, 12, 43, 10, 992616, tzinfo=utc), verbose_name=b'Run start time ')),
                ('starttime1', models.TimeField(default=datetime.timedelta(0), verbose_name=b'Beam stopper opening time ', blank=True)),
                ('starttime2', models.TimeField(default=datetime.timedelta(0), verbose_name=b'Beam stopper open ', blank=True)),
                ('endtime', models.DateTimeField(default=datetime.timedelta(0), verbose_name=b'Run stop time ')),
                ('comments', models.TextField(verbose_name=b'Comments ', blank=True)),
                ('runtype', models.CharField(max_length=10, verbose_name=b'Run type ', choices=[(b'test', b'test'), (b'signal', b'signal'), (b'pedestal', b'pedestal'), (b'tlu_no_handshare', b'tlu_no_handshake'), (b'find_shadow', b'find_shadow')])),
                ('dia1', models.CharField(default=logger.models.getPrevDiamond1, max_length=200, verbose_name=b'Diamond 1 ', choices=[(b'II6-B2', b'II6-B2'), (b'II6-94', b'II6-94'), (b'II6-95', b'II6-95'), (b'II6-96', b'II6-96'), (b'II6-97', b'II6-97'), (b'II6-A0', b'II6-A0'), (b'A', b'A'), (b'B', b'B'), (b'D', b'D'), (b'S129', b'S129'), (b'other', b'other')])),
                ('dia2', models.CharField(default=logger.models.getPrevDiamond2, max_length=200, verbose_name=b'Diamond 2 ', choices=[(b'II6-B2', b'II6-B2'), (b'II6-94', b'II6-94'), (b'II6-95', b'II6-95'), (b'II6-96', b'II6-96'), (b'II6-97', b'II6-97'), (b'II6-A0', b'II6-A0'), (b'A', b'A'), (b'B', b'B'), (b'D', b'D'), (b'S129', b'S129'), (b'other', b'other')])),
                ('maskfile', models.CharField(max_length=200, verbose_name=b'Mask file ')),
                ('dia1hv', models.IntegerField(verbose_name=b'Diamond 1 high voltage [V] ')),
                ('dia2hv', models.IntegerField(verbose_name=b'Diamond 2 high voltage [V] ')),
                ('fs11', models.IntegerField(verbose_name=b'FS11 setting [mm] ')),
                ('fs13', models.IntegerField(verbose_name=b'FS13 setting [mm] ')),
                ('quadrupole', models.IntegerField(verbose_name=b'Quadrupole setting [%] ')),
                ('rawrate', models.PositiveIntegerField(verbose_name=b'Raw rate [Hz] ')),
                ('prescaledrate', models.PositiveIntegerField(verbose_name=b'Prescaled rate [Hz] ')),
                ('TLUrate', models.PositiveIntegerField(verbose_name=b'TLU rate [Hz] ')),
                ('pulserrate', models.PositiveIntegerField(verbose_name=b'Pulser rate [Hz] ')),
                ('aimedflux', models.PositiveIntegerField(verbose_name=b'Aimed flux [kHz]')),
                ('measuredflux', models.PositiveIntegerField(verbose_name=b'Measured flux [kHz] ')),
            ],
        ),
    ]
