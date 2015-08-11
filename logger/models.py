from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core import serializers
import os
import json
from django.core.serializers.json import DjangoJSONEncoder


ZERO = timedelta(0)
jfile = "run_log.json"

def getPrevRunNumber():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return (pentry[len(pentry)-1].runnr + 1)
    return 1


def getPrevPersons():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return pentry[len(pentry)-1].persons
    return

def getPrevDiamond1():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return pentry[len(pentry)-1].dia1
    return

def getPrevDiamond2():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return pentry[len(pentry)-1].dia2
    return


class RunInfo(models.Model):
    global ZERO
    persons = models.CharField("Persons on shift ", max_length=200, default=getPrevPersons, blank=False)
    runnr = models.PositiveIntegerField("Run number ", default = getPrevRunNumber, blank=False)
    starttime0 = models.DateTimeField("Run start time ", default=timezone.now(), blank=False)
    starttime1 = models.TimeField("Beam stopper opening time ", default=ZERO, blank=True)
    starttime2 = models.TimeField("Beam stopper open ", default=ZERO, blank=True)
    endtime = models.DateTimeField("Run stop time ", default=ZERO, blank=False)
    comments = models.TextField("Comments ", blank=True)
    TEST = 'test'
    SIGNAL = 'signal'
    PEDESTAL = 'pedestal'
    TLU = 'tlu_no_handshare'
    SHADOW = 'find_shadow'
    RUN_TYPES=(
        (TEST, 'test'),
        (SIGNAL, 'signal'),
        (PEDESTAL, 'pedestal'),
        (TLU, 'tlu_no_handshake'),
        (SHADOW, 'find_shadow'),
        )
    runtype = models.CharField("Run type ", max_length=10, choices=RUN_TYPES, blank=False)
    DIAMONDS =(
    	('II6-B2', 'II6-B2'),
    	('II6-94', 'II6-94'),
    	('II6-95', 'II6-95'),
    	('II6-96', 'II6-96'),
    	('II6-97', 'II6-97'),
    	('II6-A0', 'II6-A0'),
    	('A', 'A'),
    	('B', 'B'),
    	('D', 'D'),
    	('S129', 'S129'),
    	('other', 'other'),)
    dia1 = models.CharField("Diamond 1 ", max_length=200, choices=DIAMONDS, default=getPrevDiamond1, blank=False)
    dia2 = models.CharField("Diamond 2 ", max_length=200, choices=DIAMONDS, default=getPrevDiamond2, blank=False)
    maskfile = models.CharField("Mask file ", max_length=200, blank=False)
    dia1hv = models.IntegerField("Diamond 1 high voltage [V] ", blank=False)
    dia2hv = models.IntegerField("Diamond 2 high voltage [V] ", blank=False)
    fs11 = models.IntegerField("FS11 setting [mm] ", blank=False)
    fs13 = models.IntegerField("FS13 setting [mm] ", blank=False)
    quadrupole = models.IntegerField("Quadrupole setting [%] ", blank=False)
    rawrate = models.PositiveIntegerField("Raw rate [Hz] ",  blank=False)
    prescaledrate = models.PositiveIntegerField("Prescaled rate [Hz] ", blank=False)
    TLUrate = models.PositiveIntegerField("TLU rate [Hz] ", blank=False)
    pulserrate = models.PositiveIntegerField("Pulser rate [Hz] ", blank=False)
    aimedflux = models.PositiveIntegerField("Aimed flux [kHz]", blank=False)
    measuredflux = models.PositiveIntegerField("Measured flux [kHz] ", blank=False)

    def __unicode__(self):
        return str(self.runnr)

    #overriding the save method to store data in a JSON file additionally to the data in the DB
    def save(self, *args, **kwargs):
        super(RunInfo, self).save(*args, **kwargs)

        ###~~~~Create the JSON file~~~~###
        with open("outputfile.json", "w") as out:
            raw_data = serializers.serialize('python', RunInfo.objects.all())
            actual_data = [d['fields'] for d in raw_data] #get what really matters without additional django fields
            output = json.dumps(list(actual_data), cls=DjangoJSONEncoder) #dump it to json (complicated due to datetime format (not iso))
            parsed = json.loads(output) #load string converted json file again
            sanitized = json.dumps(parsed, indent=2, sort_keys=False) #and format it nicely, sorting not required
            out.write(sanitized)
