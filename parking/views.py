from django.shortcuts import render
from django.http import HttpResponse

def get_address(request):
    return HttpResponse('get_address view')
