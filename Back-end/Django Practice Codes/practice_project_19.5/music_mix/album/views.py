from django.shortcuts import render,redirect
from . import forms
from . import models
from album.forms import AlbumForm
from album.models import Album


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

def edit_album(request, id):
  album = Album.objects.filter(id=id).first()
  form = AlbumForm(instance=album)
  if request.method == "POST":
    form = AlbumForm(request.POST, instance=album)
    
    if form.is_valid():
      form.save()
    return redirect('home')
  return render(request, './album/add_album.html', {"form": form})
 

def delete_album(req,id):
  album = models.album.objects.get(pk=id)
  album.delete()
  return redirect('home')