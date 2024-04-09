from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello World')

def login(request):
    return HttpResponse('Log in:')