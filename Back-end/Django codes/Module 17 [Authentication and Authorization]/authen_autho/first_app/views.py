from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(req):
    return render(req, './home.html')
def signup(req):
    if(not req.user.is_authenticated):
        if(req.method == 'POST'):
            form = RegisterForm(req.POST)
            if (form.is_valid()):
                messages.success(req, 'Account created successful!')      
                # messages.warning(req, 'Warning!')      
                # messages.info(req, 'Danger!')       
                form.save()
                print(form.cleaned_data)
                # return render(req, './signup.html', {'form': form, 'success': True})
        else:
            form = RegisterForm()
        return render(req, 'signup.html',{'form':form})
    else:
        return redirect('profile')

def user_login(req):
    if(not req.user.is_authenticated):

        if(req.method == 'POST'):
            form = AuthenticationForm(request=req, data=req.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name,password = userpass) #checking if the user is in database or not
                if user is not None:
                    login(req, user)
                    return redirect('profile')
                #     return render(req, './home.html')
                # else:
                #     messages.error(req, 'Invalid credentials!')
        else:
            form = AuthenticationForm()
        return render(req, 'login.html', {'form': form})
    else:
        return redirect('profile')

def profile(req):
    if(req.user.is_authenticated):
        return render(req,'profile.html',{'user':req.user})
    else:
        return redirect('login')
def user_logout(req):
    logout(req)
    return redirect('login')
