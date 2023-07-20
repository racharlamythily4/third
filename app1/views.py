from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>This is my first github project</h1>')
 
def second(request):
    return HttpResponse("<h3>This is my first-second github project</h3>")
