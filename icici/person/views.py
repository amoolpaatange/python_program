from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show12(r):
    return HttpResponse('<h1> welcome to person<h1>')