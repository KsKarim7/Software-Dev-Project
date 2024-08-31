from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
# from posts.models import Post
from django.contrib import messages

def home(req):
    return render(req, 'home.html')

def register(req):
    if req.method == 'POST':
        register_form = forms.RegistrationForm(req.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(req, 'Your account has been registered successfully')
            return redirect('home')
    
    else:
        register_form = forms.RegistrationForm()
    return render(req, 'register.html', {'form' : register_form, 'type' : 'Register'})

def user_login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_pass)
            if(user is not None):
                messages.success(req, 'You have been logged in successfully')
                login(req,user)
                return redirect('profile')
            else:
                messages.warning(req,'Your login credentials are incorrect')
                return redirect('register')
    else:
        form = AuthenticationForm()
        return render(req,'register.html',{'form':form,'type':'Login'})
    

def user_logout(req):
    logout(req)
    messages.danger(req,'You have been logged out')
    return redirect('user_login')

@login_required
def profile(req):
    if req.method == 'POST':
        profile_form = forms.ChangeUserCredential(req.POST,instance = req.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(req, 'Your profile has been updated successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserCredential(instance = req.user)
    return render(req, 'profile.html', {'form' : profile_form})

def pass_change(req):
    if req.method == 'POST':
        form = PasswordChangeForm(req.user,data = req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Password has been changed')
            update_session_auth_hash(req, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=req.user)
    return render(req, 'pass_change.html', {'form' : form})