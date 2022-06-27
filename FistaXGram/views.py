from http.client import ImproperConnectionState
from django.http import HttpResponse


from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse('hello test')