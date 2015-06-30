from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import RunInfo

def index(request):
    return HttpResponse("hello world!")

def detail(request, runnr):
    info = get_object_or_404(RunInfo, pk=runnr)
    return HttpResponse("On shift: %s " %info.persons)

    
