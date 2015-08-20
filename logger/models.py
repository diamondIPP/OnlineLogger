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

def getPrevVoltage1():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return pentry[len(pentry)-1].dia1hv
    return

def getPrevVoltage2():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return pentry[len(pentry)-1].dia2hv
    return

def getPrevMaskFile():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return pentry[len(pentry)-1].maskfile
    return    




class RunInfo(models.Model):
    global ZERO
    persons = models.CharField("Persons on shift ", max_length=200, default=getPrevPersons, blank=False)
    runnr = models.PositiveIntegerField("Run number ", default = getPrevRunNumber, blank=False)
    
    starttime0 = models.DateTimeField("Run start time ", default=ZERO, blank=False)
    starttime1 = models.TimeField("Beam stopper opening time ", default=ZERO, blank=True)
    starttime2 = models.TimeField("Beam stopper open ", default=ZERO, blank=True)
    endtime = models.DateTimeField("Run stop time ", default=ZERO, blank=False)
    
    TEST = 'test'
    SIGNAL = 'signal'
    PEDESTAL = 'pedestal'
    TLU = 'tlu_no_handshare'
    SHADOW = 'find_shadow'
    RATE = 'rate_scan'
    RUN_TYPES=(
        (TEST, 'test'),
        (SIGNAL, 'signal'),
        (PEDESTAL, 'pedestal'),
        (TLU, 'tlu no handshake'),
        (SHADOW, 'find shadow'),
        (RATE, 'rate scan')
        )
    runtype = models.CharField("Run type ", max_length=10, choices=RUN_TYPES, blank=False)
    
    DIAMONDS =(
        ('---', '---'),
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
    maskfile = models.CharField("Mask file ", max_length=200, default=getPrevMaskFile, blank=False)
    dia1hv = models.FloatField("Diamond 1 high voltage [V] ", default=getPrevVoltage1, blank=False)
    dia2hv = models.FloatField("Diamond 2 high voltage [V] ", default=getPrevVoltage2, blank=False)
    
    fs11 = models.FloatField("FS11 setting [steps] ", blank=False)
    fs13 = models.FloatField("FS13 setting [steps] ", blank=False)
    quadrupole = models.IntegerField("Quadrupole setting [%] ", blank=False)
    
    rawrate = models.PositiveIntegerField("Raw rate [Hz] ",  blank=False)
    measuredflux = models.FloatField("Measured flux [kHz/sqcm] ", blank=False)
    prescaledrate = models.PositiveIntegerField("Prescaled rate [Hz] ", blank=False)
    pulserrate = models.PositiveIntegerField("Pulser rate [Hz] ", blank=False)
    accepted_pulserrate = models.PositiveIntegerField("Accepted pulser rate [Hz] ", blank=False)
    tlu_input_rate = models.PositiveIntegerField("TLU input rate [Hz] ", blank=False)
    for1 = models.PositiveIntegerField("Fast OR 1 [Hz] ", blank=False)
    for2 = models.PositiveIntegerField("Fast OR 2 [Hz] ", blank=False)

    comments = models.TextField("Comments ", blank=True)

    

    def __unicode__(self):
        return str(self.runnr)

    #overriding the save method to store data in a JSON file additionally to the data in the DB
    def save(self, *args, **kwargs):
        super(RunInfo, self).save(*args, **kwargs)

        ###~~~~Create the JSON file~~~~###
        with open("outputfile.json", "w") as out:
            raw_data = serializers.serialize('python', RunInfo.objects.all())
            extracted_data = [{d['fields']['runnr']:d['fields']} for d in raw_data]           
            output = json.dumps(extracted_data, cls=DjangoJSONEncoder, indent=2, sort_keys=True) #dump it to json (complicated due to datetime format (not iso))
            out.write(output)
















