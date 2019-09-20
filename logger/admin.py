from django.contrib import admin
from .models import RunInfo


class RunInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General run information', {'fields': ['persons', 'runnr', 'momentum', 'starttime0', 'endtime', 'runtype', 'maskfile']}),
        ('Information about Diamond 1', {'fields': ['dia1', 'att_dia1', 'att_pul1', 'dia1hv', 'dia1supply']}),
        ('Information about Diamond 2', {'fields': ['dia2', 'att_dia2', 'att_pul2', 'dia2hv', 'dia2supply']}),
        ('Information about Diamond 3', {'fields': ['dia3', 'att_dia3', 'att_pul3', 'dia3hv', 'dia3supply']}),
        ('Beam information', {'fields': ['fs11', 'fs13']}),
        ('Rate information', {'fields': ['for1', 'for2']}),
        ('Comments', {'fields': ['comments']}),
    ]


admin.site.register(RunInfo, RunInfoAdmin)
