from django.shortcuts import render

# Create your views here.

def kids(req):
    return render(req,'navigation/kids.html')

def mens(req):
    return render(req,'navigation/mens.html')
    
def womens(req):
    return render(req,'navigation/womens.html')
