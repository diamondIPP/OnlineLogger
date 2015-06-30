from django.db import models
from django.utils import timezone


class RunInfo(models.Model):
    persons = models.CharField("Persons on shift: ", max_length=200)
    runnr = models.PositiveIntegerField("Run number: ", default =0)
    date = models.DateField("Date: ", default=timezone.now)
    time = models.TimeField("Time: ", default=timezone.now)
    comments = models.TextField("Comments: ", default="")
    TEST = 'test'
    SIGNAL = 'signal'
    PEDESTAL = 'pedestal'
    RUN_TYPES=(
        (TEST, 'test'),
        (SIGNAL, 'signal'),
        (PEDESTAL, 'pedestal'),
        )
    runtype = models.CharField(max_length=10, choices=RUN_TYPES, default=TEST)
    maskfile = models.CharField("Mask file: ", max_length=200, default = "")
    dia1 = models.CharField("Diamond 1: ", max_length=200, default = "")
    dia2 = models.CharField("Diamond 2: ", max_length=200, default = "")
    dia1hv = models.CharField("Diamond 1 high voltage: ", max_length=200, default = "")
    dia2hv = models.CharField("Diamond 2 high voltage: ", max_length=200, default = "")
    fs11 = models.IntegerField("FS11 setting: ", default = 0)
    fs13 = models.IntegerField("FS13 setting: ", default = 0)
    quadrupole = models.IntegerField("Quadrupole setting in %: ", default= 100)
    rawrate = models.PositiveIntegerField("Raw rate in Hz: ", default = 0)
    prescaledrate = models.PositiveIntegerField("Prescaled rate in Hz: ", default = 0)
    TLUrate = models.PositiveIntegerField("TLU rate in Hz: ", default = 0)
    pulserrate = models.PositiveIntegerField("Pulser rate in Hz: ", default = 0)
    aimedflux = models.PositiveIntegerField("Aimed flux: ", default = 0)
    measuredflux = models.PositiveIntegerField("Measured flux: ", default = 0)

    def __unicode__(self):
        return str(self.runnr)
    
