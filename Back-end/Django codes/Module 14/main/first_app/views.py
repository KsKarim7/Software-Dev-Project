from django.shortcuts import render,redirect
from . import models

# Create your views here.
def home(req):
    student = models.Student.objects.all()
    return render(req,"home.html",{'data':student})

def delete_student(req,roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect("homepage")
