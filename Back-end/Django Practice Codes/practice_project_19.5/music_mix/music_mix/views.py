from django.shortcuts import render
from album.models import Album
from musician.models import Musician

# Create your views here.
def home(req):
    data = Album.objects.all()
    # print(musician)
    # print(album,musician)
    # return render(req,'home.html',{'album':album},{'musician':musician})
    return render(req,'home.html',{'data':data})