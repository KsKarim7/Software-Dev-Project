from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages


# Create your views here.
def register(req):
    if(req.method == 'POST'):
        register_form = forms.AuthorForm(req.POST)
        if(register_form.is_valid()):
            register_form.save()
            messages.success(req,'Your account has been registered')
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(req, 'register.html',{'form':register_form,'type':'Register'})