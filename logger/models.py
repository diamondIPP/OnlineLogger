from django.db import models
from functools import partial
from config.config import *
from os.path import dirname, realpath, join

Dir = dirname(realpath(__file__))
DUTNr = 0


def reset_dut_nr():
    global DUTNr
    DUTNr = 0


def get_latest_(field):
    return None if not RunInfo.objects.count() else getattr(RunInfo.objects.latest('runnr'), field)


def get_latest(field):
    return partial(get_latest_, field)


def get_new_runnr():
    return 1 if not RunInfo.objects.count() else RunInfo.objects.latest('starttime0').runnr + 1


class RunInfo(models.Model):
    CONFIGFILE = join(dirname(Dir), 'config', 'config.ini')

    # GENERAL info
    runnr = models.PositiveIntegerField('Run number', default=get_new_runnr, blank=False)
    runtype = models.CharField('Run type ', max_length=20, choices=Config(CONFIGFILE).items('Run Types'), default=get_latest('runtype'), blank=False)
    persons = models.CharField('Persons on shift', max_length=200, default=get_latest('persons'), blank=False)
    starttime0 = models.DateTimeField('Run start time', blank=False)
    endtime = models.DateTimeField('Run stop time', blank=False)
    maskfile = models.CharField('Mask File ', max_length=200, default=get_latest('maskfile'), blank=False)

    # BEAM info
    momentum = models.PositiveIntegerField('Pion Momentum [MeV/c]', default=get_latest('momentum'), blank=False)
    fs11 = models.FloatField('FS11(l/r) setting [steps] ', blank=False)
    fs13 = models.FloatField('FS13 setting [steps] ', blank=False)

    # RATE info
    for1 = models.PositiveIntegerField('Fast OR Plane 2 [Hz] ', blank=False)
    for2 = models.PositiveIntegerField('Fast OR Plane 3 [Hz] ', blank=False)

    comments = models.TextField('Comments ', blank=True)

    def __str__(self):
        return f'Run {self.runnr:>03}'

    def __unicode__(self):
        return str(self.runnr)


def get_latest_dut_(field, increment=False):
    if not DUT.objects.count() or not RunInfo.objects.count():
        return
    r = RunInfo.objects.latest('runnr')
    n_duts = len(DUT.objects.filter(runinfo=r.id))
    global DUTNr
    dut_nr = DUTNr
    DUTNr += 1 if increment else 0
    return getattr(r.dut_set.all()[(dut_nr - 2) % n_duts], field) if n_duts else None


def get_latest_dut(field, increment=False):
    return partial(get_latest_dut_, field, increment)


class DUT(models.Model):
    runinfo = models.ForeignKey(RunInfo, on_delete=models.CASCADE)

    dia = models.CharField('Name', max_length=200, choices=get_duts(RunInfo.CONFIGFILE), default=get_latest_dut('dia'), blank=False)
    diasupply = models.CharField('HV Supply ', max_length=4, choices=get_hv_supplies(RunInfo.CONFIGFILE), default=get_latest_dut('diasupply'), blank=False)
    diahv = models.FloatField('High Voltage [V]', default=get_latest_dut('diahv'), blank=False)
    att_dia = models.CharField('Attenuator', max_length=200, choices=get_attenuators(RunInfo.CONFIGFILE), default=get_latest_dut('att_dia'), blank=False)
    att_pul = models.CharField('Pulser Attenuator', max_length=200, choices=get_attenuators(RunInfo.CONFIGFILE), default=get_latest_dut('att_pul', increment=True), blank=False)

    def __str__(self):
        return f'#{self.pk}'
