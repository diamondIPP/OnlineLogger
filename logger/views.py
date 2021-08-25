from django.shortcuts import render, get_object_or_404
from logger.models import RunInfo
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'logger/index.html'
    context_object_name = 'latest_run_logs'

    def get_queryset(self):
        """Return the last 20 run logs."""
        return RunInfo.objects.order_by('-pk')[:20]


def get_field_display(model, exclude=()):
    fields = [field.name for field in model._meta.get_fields() if field.name not in ('id',) + exclude]
    values = [getattr(model, f'get_{field}_display')() if hasattr(model, f'get_{field}_display') else getattr(model, field) for field in fields]
    return {model._meta.get_field(field).verbose_name: value for field, value in zip(fields, values)}


def detail(request, runnr):
    runinfo = get_object_or_404(RunInfo, runnr=runnr)
    duts = [get_field_display(dut, exclude=('runinfo',)) for dut in runinfo.dut_set.all()]
    run_display = get_field_display(runinfo, exclude=('dut', 'runnr'))
    return render(request, 'logger/detail.html', {'runinfo': run_display, 'duts': duts, 'run': runinfo.runnr})


def all_(request):
    results = [{'run': runinfo.runnr,
                'runinfo': get_field_display(runinfo, exclude=('dut', 'runnr')),
                'duts': [get_field_display(dut, exclude=('runinfo',)) for dut in runinfo.dut_set.all()]} for runinfo in RunInfo.objects.all()]
    return render(request, 'logger/all.html', {'results': results})
