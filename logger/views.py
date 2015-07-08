from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import RunInfo

def index(request):
    return HttpResponse("hello world!")

def detail(request, runnr):
    item = get_object_or_404(RunInfo, pk=runnr)
    return render(request, 'logger/detail.html', {'item':item})

def all(request):
    results = list(RunInfo.objects.all())
    return render(request, 'logger/all.html', {'results':results})
    
