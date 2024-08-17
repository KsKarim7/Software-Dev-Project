from django.shortcuts import render
import datetime

# Create your views here.
def home(req):
    dict = {'author':'Karim','age':23, 'lst':['python','is','the','best'],'birthday':datetime.datetime.now(),'courses' :[{
        'id' :1,
        'name': 'Django',
        'fee':5000
    },
    {
        'id' :2,
        'name': 'Nodejs',
        'fee' : 6000
    },
    {
        'id' :3,
        'name': 'DSA',
        'fee' : 3000
    }
    ]}
    # return render(req,'home.html',{'author':'Karim','age':23});
    return render(req,'home.html',dict);
