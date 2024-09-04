from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from musician.forms import MusicianForm
from musician.models import Musician
from album.models import Musician
from django.views.generic import CreateView,UpdateView,DeleteView

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

class AddMusicianView(CreateView):
  model = models.Musician
  form_class = forms.MusicianForm
  template_name = 'add_musician.html'
  success_url = reverse_lazy('add_musician') 
  def form_valid(self, form):
    return super().form_valid(form)
  
class EditMusicianView(UpdateView):
  model = models.Musician
  form_class = forms.MusicianForm
  template_name = 'add_musician.html'
  pk_url_kwarg = 'id'
  success_url = reverse_lazy('home') 

class DeleteMusicianView(DeleteView):
  model = models.Musician
  template_name = 'delete.html'
  success_url = reverse_lazy('home') 
  pk_url_kwarg = 'id'


def edit_musician(request, id):
  musician = Musician.objects.get(pk=id)
#   print(musician)
  form = MusicianForm(instance=musician)
  if request.method == "POST":
    form = MusicianForm(request.POST, instance=musician)
    if form.is_valid():
      form.save()
    return redirect('home')
  return render(request, 'musician', {"form": form})


def delete_musician(req,id):
    musician = models.musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')