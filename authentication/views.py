from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'authentication/login.html')

def forgot(request):
    return render(request,'authentication/forgot.html')

def register(request):
    return render(request,'authentication/register.html')

def contact(request):
    return render(request,'authentication/contact.html')

def home(request):
    #Authentication
    username=request.POST['uname']
    password=request.POST['passwd']
    if username == 'Roheeth' and password == 'RK123':
        return render(request,'authentication/home.html')
    else:
        return HttpResponse('Invalid Credentials')