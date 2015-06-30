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
    

    def __unicode__(self):
        return str(self.runnr)
    
