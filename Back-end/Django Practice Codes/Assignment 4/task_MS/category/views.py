from django.shortcuts import render

# Create your views here.

def add_category(req):
    return render(req,'add_category.html')
