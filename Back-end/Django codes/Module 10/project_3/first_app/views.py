from django.shortcuts import render

# Create your views here.
def home(req):
    dict = {'author':'Karim','age':23}
    # return render(req,'home.html',{'author':'Karim','age':23});
    return render(req,'home.html',dict);
