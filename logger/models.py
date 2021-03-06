from django.db import models
from datetime import timedelta
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

ZERO = timedelta(0)
jfile = "run_log.json"

def getPrevRunNumber():
    pentry = RunInfo.objects.all()
    if len(pentry) > 0:
        return (pentry[len(pentry)-1].runnr + 1)
    return 1

def get_previous_momentum():
    pentry = RunInfo.objects.all()
    return (pentry[len(pentry) - 1].momentum) if len(pentry) else None


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

def getPrevAtt1():
    pentry = RunInfo.objects.all()
    return pentry[len(pentry) - 1].att_dia1 if len(pentry) else None

def getPrevAtt2():
    pentry = RunInfo.objects.all()
    return pentry[len(pentry) - 1].att_dia2 if len(pentry) else None

def getPrevPulserAtt1():
    pentry = RunInfo.objects.all()
    return pentry[len(pentry) - 1].att_pul1 if len(pentry) else None

def getPrevPulserAtt2():
    pentry = RunInfo.objects.all()
    return pentry[len(pentry) - 1].att_pul2 if len(pentry) else None

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
    momentum = models.PositiveIntegerField("Pion Momentum [MeV/c]", default = get_previous_momentum, blank=False)

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
        (RATE, 'rate scan'),
        (VOLTAGE_SCAN, 'voltage scan'),
        ('shadow', 'find shadow'),
        ('pumping', 'pumping'),
        (SCHROTT, 'schrott'),
        ('p-scan', 'momentum scan'),
        ('crap', 'crap')
        )
    runtype = models.CharField("Run type ", max_length=20, choices=RUN_TYPES, default=getPrevRunType, blank=False)
    
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
        ('II6-B0', 'II6-B0'),
        ('II6-H8', 'II6-H8'),
        ('II6-H9', 'II6-H9'),
        ('II6-B6', 'II6-B6'),
        ('A', 'A'),
        ('B', 'B'),
        ('D', 'D'),
        ('2A87-E', '2A87-E'),
        ('IIa-1', 'IIa-1'),
        ('IIa-2', 'IIa-2'),
        ('IIa-3', 'IIa-3'),
        ('IIa-5', 'IIa-5'),
        ('Higgs', 'Higgs'),
        ('Einstein', 'Einstein'),
        ('Dirac', 'Dirac'),
        ('Heisenberg', 'Heisenberg'),
        ('S30', 'S30'),
	('S49', 'S49'),
        ('S83', 'S83'),
        ('S97', 'S97'),
        ('S108', 'S108'),
        ('S116', 'S116'),
	('S125', 'S125'),
        ('S129', 'S129'),
        ('SiD1', 'SiD1'),
        ('SiD2', 'SiD2'),
	('SiD6', 'SiD6'),
	('SiD7', 'SiD7'),
        ('SiD8', 'SiD8'), 
        ('SiD9', 'SiD9'),
        ('H0', 'H0'),
        ('H0-1', 'H0-1'),
        ('H0-2', 'H0-2'),
        ('H0-3', 'H0-3'),
        ('H0-4', 'H0-4'),
        ('H0-5', 'H0-5'),
        ('II6-E5', 'II6-E5'),
        ('II6-E5-3', 'II6-E5-3'),
        ('D8','D8'),
        ('L100', 'L100'),
        ('CMS01', 'CMS01'),
        ('CMS02', 'CMS02'),
        ('CMS04', 'CMS04'),
        ('BCMPrime', 'BCMPrime'),
        ('BCMPrime-C1', 'BCMPrime-C1'),
        ('BCMPrime-C2', 'BCMPrime-C2'),
        ('other', 'other'),)


    HV_SUPPLIES = (
        ('0', '---'),
        ('1-0', 'HV1-CH0'),
        ('1-1', 'HV1-CH1'),
        ('1-2', 'HV1-CH2'),
        ('1-3', 'HV1-CH3'),
        ('1-4', 'HV1-CH4'),
        ('1-5', 'HV1-CH5'),
        ('2-0', 'HV2-CH0'),
        ('2-1', 'HV2-CH1'),
        ('2-2', 'HV2-CH2'),
        ('2-3', 'HV2-CH3'),
        ('2-4', 'HV2-CH4'),
        ('2-5', 'HV2-CH5'),
        ('2', 'HV2'),
        ('3', 'HV3'), 
        ('4', 'HV4'), 
        ('5', 'HV5'), 
        ('6', 'HV6'), 
	('7-0', 'HV7-CH0'),
        ('7-1', 'HV7-CH1'), 
        ('7-2', 'HV7-CH2'),
        ('7-3', 'HV7-CH3'),
        ('7-4', 'HV7-CH4'),
        ('7-5', 'HV7-CH5'),
        ('8', 'HV8'),)

    ATTENUATORS = (
        ('---', '---'),
        ('None', 'None'),
        ('6dB_1', '6dB_1'),
        ('6dB_2', '6dB_2'),
        ('6dB_3', '6dB_3'),
        ('10dB_1', '10dB_1'),
        ('20dB_1', '20dB_1'),)


    dia1 = models.CharField("Name", max_length=200, choices=DIAMONDS, default=getPrevDiamond1, blank=False)
    dia2 = models.CharField("Name", max_length=200, choices=DIAMONDS, default=getPrevDiamond2, blank=False)   
    dia1supply = models.CharField("HV Supply ", max_length=4, choices=HV_SUPPLIES, default=getPrevHVSupply1, blank=False)
    dia2supply = models.CharField("HV Supply ", max_length=4, choices=HV_SUPPLIES, default=getPrevHVSupply2, blank=False)
    maskfile = models.CharField("Mask File ", max_length=200, default=getPrevMaskFile, blank=False)
    dia1hv = models.FloatField("High Voltage [V] ", default=getPrevVoltage1, blank=False)
    dia2hv = models.FloatField("High Voltage [V] ", default=getPrevVoltage2, blank=False)
    att_dia1 = models.CharField('Attenuator', max_length=200, choices=ATTENUATORS, default=getPrevAtt1, blank=False)
    att_dia2 = models.CharField('Attenuator', max_length=200, choices=ATTENUATORS, default=getPrevAtt2, blank=False)
    att_pul1 = models.CharField('Pulser Attenuator', max_length=200, choices=ATTENUATORS, default=getPrevPulserAtt1, blank=False)
    att_pul2 = models.CharField('Pulser Attenuator', max_length=200, choices=ATTENUATORS, default=getPrevPulserAtt2, blank=False)

    fs11 = models.FloatField("FS11(l/r) setting [steps] ", blank=False)
    fs13 = models.FloatField("FS13 setting [steps] ", blank=False)
    
    #dia2area = models.FloatField("Active Pixels ", default=getPrevArea2, blank=True)
    #dia1area = models.FloatField("Active Pixels ", default=getPrevArea1, blank=True)
    #rawrate = models.PositiveIntegerField("Raw rate [Hz] ",  blank=False)
    #measuredflux = models.FloatField("Measured flux [kHz/sqcm] ", blank=False)
    #prescaledrate = models.PositiveIntegerField("Prescaled rate [Hz] ", blank=False)
    #pulserrate = models.PositiveIntegerField("Pulser rate [Hz] ", blank=False)
    #accepted_pulserrate = models.PositiveIntegerField("Accepted pulser rate [Hz] ", blank=False)
    #tlu_input_rate = models.PositiveIntegerField("TLU input rate [Hz] ", blank=False)
    for1 = models.PositiveIntegerField("Fast OR Plane 2 [Hz] ", blank=False)
    for2 = models.PositiveIntegerField("Fast OR Plane 3 [Hz] ", blank=False)

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
                run_number = d['fields']['runnr']
                runinfo = d['fields']
                new_run_info = {}
                for key, value in runinfo.iteritems():
                    if 'att' in key and value == '---':
                        continue
                    new_run_info[key] = value
                form_d[run_number] = new_run_info

            output = json.dumps(form_d, cls=DjangoJSONEncoder, indent=2, sort_keys=True) #dump it to json (complicated due to datetime format (not iso))
            out.write(output)

