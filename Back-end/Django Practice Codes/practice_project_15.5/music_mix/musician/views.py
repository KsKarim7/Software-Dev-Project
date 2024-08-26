from django.shortcuts import render
from . import forms

# Create your views here.
def add_musician(req):
    musician_form = forms.MusicianForm()
    return render(req, 'add_musician.html',{'form':musician_form})