from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def third(request):
    return HttpResponse("This is my thist github project")

def fourth(request):
    return HttpResponse('This is my third-fourth github project')