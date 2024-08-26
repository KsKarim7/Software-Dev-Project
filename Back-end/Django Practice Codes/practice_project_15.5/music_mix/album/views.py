from django.shortcuts import render

# Create your views here.

def add_album(req):
    return render(req,'add_album.html')
