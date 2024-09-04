from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from album.forms import AlbumForm
from album.models import Album
from django.views.generic import CreateView,UpdateView,DeleteView


# Create your views here.
class AddAlbumView(CreateView):
  model = models.Album
  form_class = forms.AlbumForm
  template_name = 'add_album.html'
  success_url = reverse_lazy('add_album') 
  def form_valid(self, form):
    form.instance.Musician = self.request.user
    return super().form_valid(form)

class EditAlbumView(UpdateView):
  model = models.Album
  form_class = forms.AlbumForm
  template_name = 'add_album.html'
  pk_url_kwarg = 'id'
  success_url = reverse_lazy('home') 

class DeleteAlbumView(DeleteView):
  model = models.Album
  template_name = 'delete.html'
  success_url = reverse_lazy('home') 
  pk_url_kwarg = 'id'
  



 

def delete_album(req,id):
  album = models.album.objects.get(pk=id)
  album.delete()
  return redirect('home')