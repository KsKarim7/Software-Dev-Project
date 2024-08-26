from django.shortcuts import render
from album.models import Album
from musician.models import Musician

# Create your views here.
def home(req):
    album = Album.objects.all()
    # album = Album.objects.filter(musician=req.)
    musician = Musician.objects.filter(album= album[4])
    print(musician)
    # print(album,musician)
    # return render(req,'home.html',{'album':album},{'musician':musician})
    return render(req,'home.html',{'data':musician})