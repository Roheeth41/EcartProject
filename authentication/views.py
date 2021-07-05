from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.forms import forms

otp_1=''
uname=''

# Create your views here.
def login(request):
    return render(request,'authentication/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'authentication/login.html')

def forgot(request):
    if request.method=="POST":
        global uname
        global otp_1
        uname=request.POST['username']
        emaill=request.POST['email']
        if User.objects.filter(username=uname,email=emaill).exists(): #To check if the user exists on db
            otp_1=random.randint(100000,999999)
            messages.info(request,otp_1)
            return redirect('otp')
        else:
            messages.info(request,'User doesnt exist')
            return redirect('/')
    else:
        return render(request,'authentication/forgot.html')

def register(request):
    if request.method == 'POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        uname=request.POST['username']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        emaill=request.POST['email']
        if pass1 == pass2:
            if not User.objects.filter(username=uname).exists():
                if not User.objects.filter(email=emaill).exists():
                    user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,password=pass1,email=emaill)
                    user.save()
                    return render(request,'authentication/login.html')
                else:
                    messages.info(request,'Email already exists')
                    return render(request,'authentication/register.html')
            else:
                messages.info(request,'Username already exists')
                return render(request,'authentication/register.html')
        else:
            messages.info(request,'Password doesnt match')
            return render(request,'authentication/register.html')
    else:
        return render(request,'authentication/register.html')

def contact(request):
    return render(request,'authentication/contact.html')

def home(request):
    if request.method == 'POST':
        username=request.POST['uname']
        password=request.POST['pass']
        print(username,password)
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user) #Used to login
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'authentication/login.html')
    else:
        return render(request,'authentication/home.html')

def otp(request):
    if request.method == 'POST':
        otp_2=request.POST['otp']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        print(otp_1,otp_2,type(otp_1),type(otp_2),uname,pass1)
        if otp_1 == int(otp_2):
            if pass1 == pass2:
                user=User.objects.get(username=uname)
                user.set_password(pass1)
                user.save()
                messages.info(request,'Password is succesfully changed. Login to continue..')
                return redirect('login')
            else:
                messages.info(request,'Password doesnt match')
                return redirect('login')
        else:
            messages.info(request,'OTP doesnt match')
            return redirect('login')
    else:
        return render(request,'authentication/otp.html')