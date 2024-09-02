from django.shortcuts import render,redirect
from . import forms

# Create your views here.


def add_category(req):
    if(req.method == 'POST'):  #user post request
        category_form = forms.CategoryForm(req.POST)  # capturing the post request data of the user
        if(category_form.is_valid()):  # validation of the posted data
            category_form.save()  # if the data valid then it is set in the database
            return redirect('add_category')  #then sending data to add_category url if everything is good
    else:  #or else user will get blank form 
        category_form = forms.CategoryForm(req.POST)

    return render(req,'add_category.html',{'form':category_form})