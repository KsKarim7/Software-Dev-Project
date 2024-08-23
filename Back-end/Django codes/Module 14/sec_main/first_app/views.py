from django.shortcuts import render
from first_app.forms import StudentForm

# Create your views here.
def home(req):
    # std =StudentForm()
    if(req.method == 'POST'):
        form = StudentForm(req.POST)
        if(form.is_valid()):
            form.save(commit = False)

    else:
        form = StudentForm()
    return render(req, 'home.html',{'form': form})
