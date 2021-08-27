from django.contrib import admin
from logger.models import RunInfo, DUT, Dir, json, join, dirname, Config, reset_dut_nr
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import ModelForm


class AlwaysChangedModelForm(ModelForm):

    # return always true, such that the DUTs are added to each run info even if no changes were made
    def has_changed(self):
        return True

    # overriding the save method to store data in a JSON file additionally to the data in the DB
    def _save_m2m(self):
        super(AlwaysChangedModelForm, self)._save_m2m()
        save_json()


class DUTInline(admin.StackedInline):
    form = AlwaysChangedModelForm
    model = DUT
    extra = Config(RunInfo.CONFIGFILE).getint('Main', 'n duts')
    verbose_name = 'DUT'
    verbose_name_plural = 'DUT Information'


class ChangeInline(DUTInline):
    extra = 0


@admin.register(RunInfo)
class RunInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General run information', {'fields': ['runnr', 'runtype', 'persons', 'starttime0', 'endtime', 'maskfile']}),
        ('Beam information', {'fields': ['momentum', 'fs11', 'fs13']}),
        ('Rate information', {'fields': ['for1', 'for2']}),
        ('Comments', {'fields': ['comments']}),
    ]
    inlines = []
    list_filter = ['starttime0']
    list_display = ['runnr', 'starttime0', 'fs11', 'fs13']
    # search_fields = ['dia1']

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.inlines = [ChangeInline, ]
        return super(RunInfoAdmin, self).change_view(request, object_id, form_url='', extra_context=None)

    def add_view(self, request, form_url='', extra_context=None):
        self.inlines = [DUTInline, ]
        reset_dut_nr()
        return super(RunInfoAdmin, self).add_view(request, form_url='', extra_context=None)


def save_json():
    with open(join(dirname(Dir), 'run_log.json'), 'w') as f:
        run_infos = serializers.serialize('python', RunInfo.objects.all())
        form_d = {d['fields']['runnr']: {key: value for key, value in d['fields'].items() if key not in ['runnr']} for d in run_infos}
        for runinfo in RunInfo.objects.all():
            for i, dic in enumerate(serializers.serialize('python', runinfo.dut_set.all()), 1):
                for key, value in dic['fields'].items():
                    j = key.find('dia') + 3 if 'dia' in key else len(key)
                    if key not in ['runinfo', 'group']:
                        form_d[runinfo.runnr][f'{key[:j]}{i}{key[j:]}'] = value
        json.dump(form_d, f, cls=DjangoJSONEncoder, indent=2, sort_keys=True)  # dump it to json (complicated due to datetime format (not iso))
