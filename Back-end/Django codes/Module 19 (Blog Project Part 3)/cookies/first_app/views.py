from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.
def home(req):
    response - render(req,'home.html')
    # response.set_cookie('name','rahim',max_age=10) #10SECONDS
    response.set_cookie('name','rahim',expires = datetime.utcnow() + timedelta(days=7)) 
    return response

def get_cookie(req):
    name = req.COOKIES.get('name')
    print(req.COOKIES)
    return render(req,'get_cookie.html',{'name':name})

def delete_cookie(req):
    res = render(req,'del.html')
    res.delete_cookie('name')
    return res


def set_session(req):
    # data = {
    #     'name':'rahim',
    #     'age':25,
    #     'language':'Bengali'
    # }
    # print(req.session.get_expiry_date())
    # print(req.session.get_session_cookie_age())
    # req.session.update(data)
    # return render(req,'home.html')

    req.session['name'] = 'rahim'
    req.session['age'] = 25
    return render(req,'home.html')


def get_session(req):
    if('name' in req.session):

        name = req.session.get('name','Guest')
        age = req.session.get('age')
        req.session.modified = True
    else:
        return HttpResponse("Your session has been expired! Tada")
    # data = req.session
    return render(req,'get_session.html',{'name':name,'age':age})

def delete_session(req):
    # del req.session['name'] # for individual deletion
    req.session.flush()
    return render(req,'del.html')