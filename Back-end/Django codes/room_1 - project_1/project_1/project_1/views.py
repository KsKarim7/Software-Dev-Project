from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the home page");

def contact(request):
    return HttpResponse("This is a contact request")