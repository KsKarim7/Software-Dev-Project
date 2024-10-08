from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.


# def add_author(req):
#     if(req.method == 'POST'):
#         author_form = forms.AuthorForm(req.POST)
#         if(author_form.is_valid()):
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm(req.POST)

#     return render(req,'add_author.html',{'form':author_form})

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


# def user_login(req):
#     if req.method == 'POST':
#         form = AuthenticationForm(req, req.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username=user_name, password=user_pass)
#             if user is not None:
#                 messages.success(req, 'Logged in Successfully')
#                 login(req, user)
#                 return redirect('profile')
#             else:
#                 messages.warning(req, 'Incorrect login credentials')
#                 return redirect('register')
#     else:
#         form = AuthenticationForm()
#         return render(req, 'register.html', {'form' : form, 'type' : 'Login'})

class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid login credentials')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    

@login_required
def profile(req):
    data = Post.objects.filter(author = req.user)
    return render(req, 'profile.html', {'data' : data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})


def pass_change(req):
    if req.method == 'POST':
        form = PasswordChangeForm(req.user, data=req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Password Updated Successfully')
            update_session_auth_hash(req, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=req.user)
    return render(req, 'pass_change.html', {'form' : form})

def user_logout(request):
    logout(request)
    return redirect('user_login')


