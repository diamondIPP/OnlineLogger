from django.shortcuts import render, get_object_or_404
from logger.models import RunInfo
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'logger/index.html'
    context_object_name = 'latest_run_logs'

    def get_queryset(self):
        """Return the last five logs."""
        return RunInfo.objects.order_by('-endtime')[:20]


def detail(request, runnr):
    runinfo = get_object_or_404(RunInfo, runnr=runnr)
    return render(request, 'logger/detail.html', {'runinfo': runinfo})


def all_(request):
    results = list(RunInfo.objects.all())
    return render(request, 'logger/all.html', {'results': results})
