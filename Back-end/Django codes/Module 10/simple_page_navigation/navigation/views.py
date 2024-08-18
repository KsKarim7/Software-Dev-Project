from django.shortcuts import render

# Create your views here.

def about(req):
    return render(req,'navigation/about.html');
def contact(req):
    return render(req,'navigation/contact.html')

# def home(req):
#     pass
