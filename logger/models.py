from django.db import models
from django.utils import timezone
from datetime import timedelta


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

def saveJson():
    return
    

class RunInfo(models.Model):
    ZERO = timedelta(0)
    persons = models.CharField("Persons on shift ", max_length=200, default=getPrevPersons, blank=False)
    runnr = models.PositiveIntegerField("Run number ", default = getPrevRunNumber, blank=False)
    starttime0 = models.DateTimeField("Run start time ", default=timezone.now(), blank=False)
    starttime1 = models.TimeField("Beam stopper opening time ", default=ZERO, blank=True)
    starttime2 = models.TimeField("Beam stopper open ", default=ZERO, blank=True)
    endtime = models.DateTimeField("Run stop time ", default=0, blank=False)
    comments = models.TextField("Comments ", blank=True)
    TEST = 'test'
    SIGNAL = 'signal'
    PEDESTAL = 'pedestal'
    RUN_TYPES=(
        (TEST, 'test'),
        (SIGNAL, 'signal'),
        (PEDESTAL, 'pedestal'),
        )
    runtype = models.CharField("Run type ", max_length=10, choices=RUN_TYPES, blank=False)
    maskfile = models.CharField("Mask file ", max_length=200, blank=False)
    dia1 = models.CharField("Diamond 1 ", max_length=200, default = "", blank=False)
    dia2 = models.CharField("Diamond 2 ", max_length=200, default = "", blank=False)
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
    


    
