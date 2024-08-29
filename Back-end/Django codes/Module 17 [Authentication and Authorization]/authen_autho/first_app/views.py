from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash


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
            form = AuthenticationForm(req=req, data=req.POST)
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
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = ChangeUserData(req.POST, instance=req.user)
            if form.is_valid():
                messages.success(req, 'Account updated successfully')
                form.save()
        else:
            form = ChangeUserData(instance=req.user)
        return render(req, './profile.html', {'form': form})
    else:
        return redirect('signup')
def user_logout(req):
    logout(req)
    return redirect('login')

def pass_change(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = PasswordChangeForm(user=req.user, data=req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(req, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=req.user)
        return render(req, 'passchange.html', {'form': form})
    else:
        return redirect('login')
    

def pass_change2(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = SetPasswordForm(user=req.user, data=req.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(req, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=req.user)
        return render(req, './passchange.html', {'form': form})
    else:
        return redirect('login')


def change_user_data(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = ChangeUserData(req.POST, instance=req.user)
            if form.is_valid():
                messages.success(req, 'Account updated successfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData()
        return render(req, './profile.html', {'form': form})
    else:
        return redirect('signup')