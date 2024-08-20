from django.shortcuts import render

def home(req):
    return render(req,'home.html')
def meal(req):
    return render(req,'index.html');
def about(req):
    return render(req,'about.html');

