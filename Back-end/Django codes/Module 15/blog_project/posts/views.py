from django.shortcuts import render,redirect
from . import forms

# Create your views here.


def add_post(req):
    if(req.method == 'POST'):  #user post request
        post_form = forms.PostForm(req.POST)  # capturing the post request data of the user
        if(post_form.is_valid()):  # validation of the posted data
            post_form.save()  # if the data valid then it is set in the database
            return redirect('add_post')  #then sending data to add_post url if everything is good
    else:  #or else user will get blank form 
        post_form = forms.PostForm(req.POST)

    return render(req,'add_post.html',{'form':post_form})