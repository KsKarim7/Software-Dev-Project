from django.shortcuts import render
from . forms import contactForm,StudentData,PasswordValidationProject

# Create your views here.
def home(request):
    return render(request,'./application/home.html')
def about(req):
    if(req.method == 'POST'):
        print(req.POST)
        name = req.POST.get('username')
        email = req.POST.get('email')
        select = req.POST.get('select')
        return render(req,'./application/about.html',{'name':name, 'email':email,'select':select})
    else:
        return render(req,'./application/about.html')

def submit_form(req):
    return render(req,'./application/form.html')

def DjangoForm(req):
    if(req.method == 'POST'):
        form = contactForm(req.POST,req.FILES)
        if(form.is_valid()):
            # file = form.cleaned_data['file']
            # with open('./application/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            # return render(req,'./application/django_form.html',{'form':form})
    else:
        form = contactForm()
    return render(req,'./application/django_form.html',{'form':form})


def StudentForm(req):
    if (req.method == 'POST'):
        form = StudentData(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(req, './application/django_form.html', {'form':form})  

def PasswordValidation(req):
    if (req.method == 'POST'):
        form = PasswordValidationProject(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()
    return render(req, './application/django_form.html', {'form':form})  
