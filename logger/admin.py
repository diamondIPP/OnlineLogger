from django.contrib import admin
from .models import RunInfo

class RunInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General run information', {'fields': ['persons', 'runnr', 'starttime0', 'endtime', 'runtype']}),
        ('Information about the diamond(s)', {'fields': ['dia1', 'dia1area', 'dia1hv', 'dia1supply', 'dia2', 'dia2area', 'dia2hv', 'dia2supply', 'maskfile']}),
        ('Beam information', {'fields': ['fs11', 'fs13']}),
        ('Rate information', {'fields': ['for1', 'for2']}),
        ('Comments', {'fields': ['comments']}),
        ]


admin.site.register(RunInfo, RunInfoAdmin)
