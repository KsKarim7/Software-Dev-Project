from django.shortcuts import render
from task.models import Task

def home(req):
    data = Task.objects.all()
    # print(data)
    return render(req, 'home.html',{'data':data})