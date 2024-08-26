from django.shortcuts import render,redirect
from . import forms


# Create your views here.

def add_album(req):
    if(req.method == 'POST'):
        album_form = forms.AlbumForm(req.POST)
        if(album_form.is_valid()):
            album_form.save()
            return redirect('home')
    
    else:
        album_form = forms.AlbumForm()

    return render(req, 'add_album.html',{'form':album_form})
 