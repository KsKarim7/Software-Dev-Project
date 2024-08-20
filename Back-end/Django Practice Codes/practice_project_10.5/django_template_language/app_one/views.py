from django.shortcuts import render
import datetime

# Create your views here.
def home(req):
    dict = {'author':'Karim','institute':'BracU','age':23,
    'dictLst':[
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
    ],'pplLst':[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
    ],'numLst':[22,33,11], 'lst':['C++','is','better'],'birthday':datetime.datetime.now(),'courses' :[{
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
    },
    {
        'id' :4,
        'name': 'SQL',
        'fee' : 2000
    },
    {
        'id' :5,
        'name': 'OOP',
        'fee' : 1000
    },
    ]}
    # return render(req,'home.html',{'author':'Karim','age':23});
    return render(req,'home.html',dict);
