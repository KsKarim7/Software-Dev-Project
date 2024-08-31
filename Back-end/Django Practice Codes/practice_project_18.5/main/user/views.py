from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate,login

def home(req):
    return render(req, 'home.html')

def register(req):
    if req.method == 'POST':
        register_form = forms.RegistrationForm(req.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(req, 'Account Created Successfully')
            return redirect('register')
    
    else:
        register_form = forms.RegistrationForm()
    return render(req, 'register.html', {'form' : register_form, 'type' : 'Register'})

    return render(req, 'register.html')

def user_login(req):
    if(req.method == 'POST'):
        form = AuthenticationForm(req,req.POST)
        if(form.is_valid):
            user_name = form.cleaned_data['user_name']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_pass)
            if(user is not None):
                login(req,user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = AuthenticationForm()
        return render(req,'register.html',{'form':form,'type':'Login'})
