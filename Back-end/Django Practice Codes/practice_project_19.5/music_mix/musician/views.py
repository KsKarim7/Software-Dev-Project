from django.shortcuts import render,redirect
from . import forms
from . import models

from musician.forms import MusicianForm
from musician.models import Musician

# Create your views here.
def add_musician(req):
    if(req.method == 'POST'):
        musician_form = forms.MusicianForm(req.POST)
        if(musician_form.is_valid()):
            musician_form.save()
            return redirect('add_musician')
    
    else:
        musician_form = forms.MusicianForm()

    return render(req, 'add_musician.html',{'form':musician_form})



def edit_musician(request, id):
  musician = Musician.objects.get(pk=id)
#   print(musician)
  form = MusicianForm(instance=musician)
  if request.method == "POST":
    form = MusicianForm(request.POST, instance=musician)
    if form.is_valid():
      form.save()
    return redirect('home')
  return render(request, './musician/add_musician.html', {"form": form})


def delete_musician(req,id):
    musician = models.musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')