from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(req):
    # return HttpResponse("This is home page");
    return render(req,'first_app/home.html');
