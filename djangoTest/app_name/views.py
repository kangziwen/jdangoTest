from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse,render,redirect

def index(request):
    return HttpResponse('ok')