from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from fernweh import emailAuth
import hashlib

def homeview(request,loginsuccess="False"):
    return render(request,'home.html')


def browseview(request):
    return render(request,'browse.html')


def aboutview(request):
    return render(request,'about.html')


def contactview(request):
    return render(request,'contact.html')

def loginview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            _email = request.POST['email']
            _password = request.POST['pass']
            user = emailAuth.EmailOrUsernameModelBackend.authenticate(request, username=_email, password=_password)
            if user is not None:
                login(request, user)
                print("################## GİRİŞ YAPILDI")
                return homeview(request, loginsuccess="true")
            else:
                print("################## AUTH ERROR")
                return render(request, 'login.html', {'error': 'yes'})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'home.html')

def signupview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            _fullname = request.POST['fullname']
            _email = request.POST['email']
            _password = request.POST['pass']
            _repass = request.POST['repass']
            if _fullname != "" and _email != "" and _password == _repass:
                name, surname = _fullname.split(' ')
                username = name + surname
                m = hashlib.md5()
                email = _email.encode('utf-8')
                m.update(email)
                if emailAuth.EmailOrUsernameModelBackend.addUser(request, username=m.hexdigest(), email=_email, password=_password,name=name, surname=surname) == "OK":
                    print("Kayit basarili")
            else:
                if _email=="":
                    return render(request, 'signup.html',{'error':'yes','fN':'yes','fullname':_fullname})
                if _fullname=="":
                    return render(request, 'signup.html', {'error':'yes','eM':'yes','email': _email})
                else:
                    return render(request, 'signup.html', {'error':'yes','eM':'yes','fN':'yes','email': _email,'fullname':_fullname})

        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'home.html')
    return render(request,"signup.html")


def signupfunc(request):
    return render(request,'login.html')

def logoutfunc(request):
    logout(request)
    return homeview(request)