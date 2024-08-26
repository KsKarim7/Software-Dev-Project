from django.shortcuts import render
from . forms import ExampleForm

# Create your views here.
# def home(req):
#     return render(req,'home.html');
def about(req):
    if(req.method == "POST"):
        name = req.POST.get('name')
        email = req.POST.get('email')
        

def DjangoForm(req):
    form = ExampleForm(req.POST)
    if(form.is_valid()):
        print(form.cleaned_data)
        # return render(req,'django_form.html',{'form':form})
    return render(req,'django_form.html',{'form':form})


def DjangoModel(req):
    return render(req,'django_model.html')
