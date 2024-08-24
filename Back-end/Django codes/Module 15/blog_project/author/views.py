from django.shortcuts import render
from . import forms

# Create your views here.


def add_author(req):
    author_form = forms.AuthorForm()
    return render(req,'add_author.html',{'form':author_form})