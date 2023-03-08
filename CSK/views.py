from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dhoni(request):
    return HttpResponse('<h1>MSD is the Best IPL captain!!')
def raina(request):
    return HttpResponse('<h1>Raina is known as MR.IPL!!')
def jadeja(request):
    return HttpResponse('<h1>Jaddu is the Best All rounder!!')