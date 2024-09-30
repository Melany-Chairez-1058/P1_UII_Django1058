from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return HttpResponse("Hola chairez respondiendo")
# Create your views here.
