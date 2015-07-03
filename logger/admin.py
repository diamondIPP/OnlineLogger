from django.contrib import admin
from .models import RunInfo

class RunInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General run information', {'fields': ['persons', 'runnr', 'starttime0','starttime1', 'starttime2', 'endtime', 'runtype']}),
        ('Information about the diamond', {'fields': ['dia1', 'dia1hv', 'dia2', 'dia2hv','maskfile']}),
        ('Beam information', {'fields': ['fs11', 'fs13', 'quadrupole']}),
        ('Rate information', {'fields': ['rawrate', 'prescaledrate', 'TLUrate', 'pulserrate', 'aimedflux', 'measuredflux']}),
        ('Comments', {'fields': ['comments']}),
        ]


admin.site.register(RunInfo, RunInfoAdmin)
