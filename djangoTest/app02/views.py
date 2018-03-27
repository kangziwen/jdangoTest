from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.shortcuts import HttpResponse,render,redirect
def login(request):
    return HttpResponse('login')