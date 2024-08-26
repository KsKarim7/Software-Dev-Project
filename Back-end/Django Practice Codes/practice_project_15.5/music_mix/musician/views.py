from django.shortcuts import render,redirect
from . import forms

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