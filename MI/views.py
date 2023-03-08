from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohit(request):
    return HttpResponse('<h1>Rohit is the best opening batsman.')
def sachin(request):
    return HttpResponse('<h1>Sachin is the best opening batsman.')
def surya(request):
    return HttpResponse('<h1>Surya is the known as Indian360 or SKY.')