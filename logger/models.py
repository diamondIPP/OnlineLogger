from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core import serializers
import os
import json
from django.core.serializers.json import DjangoJSONEncoder
import time

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

def getPrevHVSupply1():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return pentry[len(pentry)-1].dia1supply
    return

def getPrevHVSupply2():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return pentry[len(pentry)-1].dia2supply
    return

def getPrevRunType():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return pentry[len(pentry)-1].runtype
    return

def getPrevArea1():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return pentry[len(pentry)-1].dia1area
    return

def getPrevArea2():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return pentry[len(pentry)-1].dia2area
    return



class RunInfo(models.Model):
    global ZERO
    persons = models.CharField("Persons on shift ", max_length=200, default=getPrevPersons, blank=False)
    runnr = models.PositiveIntegerField("Run number ", default = getPrevRunNumber, blank=False)
    
    starttime0 = models.DateTimeField("Run start time ", default=ZERO, blank=False)
    #starttime1 = models.TimeField("Beam stopper opening time ", default=ZERO, blank=True)
    #starttime2 = models.TimeField("Beam stopper open ", default=ZERO, blank=True)
    endtime = models.DateTimeField("Run stop time ", default=ZERO, blank=False)
    
    TEST = 'test'
    SIGNAL = 'signal'
    PEDESTAL = 'pedestal'
    TLU = 'tlu_no_handshare'
    VOLTAGE_SCAN = 'voltage_scan'
    SCHROTT = 'schrott'
    SHADOW = 'find_shadow'
    RATE = 'rate_scan'
    RUN_TYPES=(
        (TEST, 'test'),
        (SIGNAL, 'signal'),
        (PEDESTAL, 'pedestal'),
        (TLU, 'tlu no handshake'),
        (VOLTAGE_SCAN, 'voltage scan'),
        (SCHROTT, 'schrott'),
        (RATE, 'rate scan')
        )
    runtype = models.CharField("Run type ", max_length=10, choices=RUN_TYPES, default=getPrevRunType, blank=False)
    
    DIAMONDS =(
        ('---', '---'),
        ('II6-B2', 'II6-B2'),
        ('II6-94', 'II6-94'),
        ('II6-95', 'II6-95'),
        ('II6-96', 'II6-96'),
        ('II6-97', 'II6-97'),
        ('II6-A0', 'II6-A0'),
        ('II6-A2', 'II6-A2'),
        ('II6-A7', 'II6-A7'),
        ('A', 'A'),
        ('B', 'B'),
        ('D', 'D'),
        ('S129', 'S129'),
        ('2A87-E', '2A87-E'),
        ('IIa-1', 'IIa-1'),
        ('IIa-2', 'IIa-2'),
        ('IIa-3', 'IIa-3'),
        ('IIa-5', 'IIa-5'),
        ('Higgs', 'Higgs'),
        ('Einstein', 'Einstein'),
        ('Dirac', 'Dirac'),
        ('Heisenberg', 'Heisenberg'),
        ('S83', 'S83'),
        ('S97', 'S97'),
        ('SiD1', 'SiD1'),
        ('SiD2', 'SiD2'),
        ('H0', 'H0'),
        ('other', 'other'),)


    HV_SUPPLIES = (
        ('0', '---'),
        ('1', 'HV1'),
        ('2', 'HV2'),
        ('3', 'HV3'), 
        ('4', 'HV4'), 
        ('5', 'HV5'), 
        ('6', 'HV6'), 
        ('7-1', 'HV7-CH1'), 
        ('7-2', 'HV7-CH2'),
        ('7-3', 'HV7-CH3'),
        ('7-4', 'HV7-CH4'),
        ('7-5', 'HV7-CH5'),
        ('8', 'HV8'),)


    dia1 = models.CharField("Diamond 1 ", max_length=200, choices=DIAMONDS, default=getPrevDiamond1, blank=False)
    dia2 = models.CharField("Diamond 2 ", max_length=200, choices=DIAMONDS, default=getPrevDiamond2, blank=False)   
    dia1supply = models.CharField("Diamond 1 HV supply ", max_length=4, choices=HV_SUPPLIES, default=getPrevHVSupply1, blank=False)
    dia2supply = models.CharField("Diamond 2 HV supply ", max_length=4, choices=HV_SUPPLIES, default=getPrevHVSupply2, blank=False)
    maskfile = models.CharField("Mask file ", max_length=200, default=getPrevMaskFile, blank=False)
    dia1hv = models.FloatField("Diamond 1 high voltage [V] ", default=getPrevVoltage1, blank=False)
    dia2hv = models.FloatField("Diamond 2 high voltage [V] ", default=getPrevVoltage2, blank=False)
    dia1area = models.FloatField("Diamond 1 active pixels ", default=getPrevArea1, blank=True)
    dia2area = models.FloatField("Diamond 2 active pixels ", default=getPrevArea2, blank=True)

    fs11 = models.FloatField("FS11 setting [steps] ", blank=False)
    fs13 = models.FloatField("FS13 setting [steps] ", blank=False)
    
    #rawrate = models.PositiveIntegerField("Raw rate [Hz] ",  blank=False)
    #measuredflux = models.FloatField("Measured flux [kHz/sqcm] ", blank=False)
    #prescaledrate = models.PositiveIntegerField("Prescaled rate [Hz] ", blank=False)
    #pulserrate = models.PositiveIntegerField("Pulser rate [Hz] ", blank=False)
    #accepted_pulserrate = models.PositiveIntegerField("Accepted pulser rate [Hz] ", blank=False)
    #tlu_input_rate = models.PositiveIntegerField("TLU input rate [Hz] ", blank=False)
    for1 = models.PositiveIntegerField("Fast OR Plane 1 [Hz] ", blank=False)
    for2 = models.PositiveIntegerField("Fast OR Plane 2 [Hz] ", blank=False)

    comments = models.TextField("Comments ", blank=True)

    

    def __unicode__(self):
        return str(self.runnr)

    #overriding the save method to store data in a JSON file additionally to the data in the DB
    def save(self, *args, **kwargs):
        super(RunInfo, self).save(*args, **kwargs)

        ###~~~~Create the JSON file~~~~###
        with open("run_log.json", "w") as out:
            raw_data = serializers.serialize('python', RunInfo.objects.all())

            form_d = {}
            for d in raw_data:
                key = d['fields']['runnr']
                runinfo = d['fields']
                form_d[key] = runinfo

            output = json.dumps(form_d, cls=DjangoJSONEncoder, indent=2, sort_keys=True) #dump it to json (complicated due to datetime format (not iso))
            out.write(output)
















