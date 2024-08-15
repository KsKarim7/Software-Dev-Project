from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courses(req):
    return HttpResponse("Coursera");
def about(req):
    return HttpResponse("This is all about me.");
def home(req):
    return HttpResponse("Home sweet home.");
