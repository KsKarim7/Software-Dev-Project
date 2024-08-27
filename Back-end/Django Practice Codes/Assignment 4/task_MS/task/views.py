from django.shortcuts import render

# Create your views here.

def add_task(req):
    return render(req, 'add_task.html')
