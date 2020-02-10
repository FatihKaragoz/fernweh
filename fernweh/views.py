from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from fernweh import emailAuth
import hashlib
import urllib, json


def homeview(request,loginsuccess="False"):
    if request.user.is_authenticated:
        url = "https://api.nasa.gov/planetary/apod?api_key=m2ZXbWaFSKZETclOc0ZbWVTnHAkBthdtSKR7gmv8"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return render(request, 'home.html', {"apod": data})
    return render(request,'home.html')


def browseview(request):
    if request.user.is_authenticated:
      return render(request,'browse.html')
    else:
        return render(request,'login.html',{"error":"browseautherror","errorinfo":"You've to login for search NASA image library, please login!","pageload":"browse"})

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
                print("##################GİRİŞ YAPILDI")
                try:
                    if request.POST['browse']!=None:
                        if request.POST['browse']=="1":
                            print("BROWSE'A GİRDİİİİİİİİİİİİİİİİİ ")
                            return render(request,'browse.html')
                except:
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


def searchfunc(request):
    if request.method == 'POST':
        url = "https://images-api.nasa.gov/search"
        control = 0
        _q = request.POST['q']
        if _q is not None and _q!="":
            splitted = str(_q).split(" ")
            parameter = ""
            if len(splitted)>1:
                for i in range(len(splitted)-1):
                    parameter+=str(splitted[i])+"%20"
                parameter+=str(splitted[len(splitted)-1])
                url = url + "?q=" + str(parameter)
            else:
                url = url + "?q=" + str(_q)
            control = 1
        #
        # _page = request.POST['page']
        # if _page is not None and _page!="":
        #     if control == 1:
        #         url = url + "&page=" + str(_page)
        #     else:
        #         url = url + "?page=" + str(_page)
        #         control = 1
        #
        _image = request.POST['image']
        if _image is not None and _image!="":
            if control == 1:
                url = url + "&media_type=image"
            else:
                url = url + "?media_type=image"
                control = 1

        # _audio = request.POST['audio']
        # if _audio is not None and _audio!="":
        #     if control == 1:
        #         url = url + "&media_type=audio"
        #     else:
        #         url = url + "?media_type=audio"
        #         control = 1

        _description = request.POST['desc']
        if _description is not None and _description!="":
            splitted = str(_description).split(" ")
            parameter = str(splitted[0])
            if len(splitted) > 1:
                parameter+="%20"
                for i in range(1, len(splitted) - 1):
                    parameter += str(splitted[i]) + "%20"
                parameter += str(splitted[len(splitted) - 1])
            if control == 1:
                url = url + "&description=" + str(parameter)
            else:
                url = url + "?description=" + str(parameter)
                control = 1

        _title = request.POST['title']
        if _title is not None and _title!="":
            splitted = str(_title).split(" ")
            parameter = str(splitted[0])
            if len(splitted) > 1:
                parameter += "%20"
                for i in range(1, len(splitted) - 1):
                    parameter += str(splitted[i]) + "%20"
                parameter += str(splitted[len(splitted) - 1])
            if control == 1:
                url = url + "&title=" + str(parameter)
            else:
                url = url + "?title=" + str(parameter)
                control = 1

        _keyword = request.POST['keyword']
        if _keyword is not None and _keyword!="":
            splitted = str(_keyword).split(" ")
            parameter = str(splitted[0])
            if len(splitted) > 1:
                parameter += "%20"
                for i in range(1, len(splitted) - 1):
                    parameter += str(splitted[i]) + "%20"
                parameter += str(splitted[len(splitted) - 1])
            if control == 1:
                url = url + "&keywords=" + str(parameter)
            else:
                url = url + "?keywords=" + str(parameter)
                control = 1

        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        print(data)
        html = ""
        jquery= "<script>" \
                    "$(document).ready(function() {"
        for record in data['collection']['items']:
            title = record['data'][0]['title']
            nasa_id = record['data'][0]['nasa_id']
            description = record['data'][0]['description']
            href = record['links'][0]['href']
            html+=" <div class=\"col-12 col-md-6 col-xl-4\">" \
                    "<div class=\"single-blog-area style-2 wow fadeInUp\" data-wow-delay=\"300ms\">" \
                  "<div class=\"single-blog-thumb\">" \
                    "<a id=\""+nasa_id+"\" href=\""+href+"\"><img src=\""+href+"\" alt=""></a>" \
                  "</div>" \
                  "<div class=\"single-blog-text text-center\">" \
                  "<a class=\"blog-title\" href=\"#\">"+title+"</a><!-- Post Meta --><div class=\"post-meta\">" \
                    "<a class=\"post-date\" href=\"#\"><i class=\"zmdi zmdi-alarm-check\"></i> January 14, 2019</a>" \
                    "<a class=\"post-author\" href=\"#\">" \
                    "<i class=\"zmdi zmdi-account\"></i> Laura Green</a></div><p>"+description+".</p>" \
                                                "</div>" \
                                                "<div class=\"blog-btn\">" \
                                                                     "<a href=\"#\">" \
                                                                     "<i class=\"zmdi zmdi-long-arrow-right\"></i></a></div>" \
                                                                                               "</div>" \
                                                                                               "</div>"
            jquery+="$(\"#"+nasa_id+"\").fancybox({openEffect	: 'elastic',closeEffect	: 'elastic',helpers : {title : { type : 'outside'}}});"

    jquery+="});</script>"


    return render(request,'results.html',{'html':html,"jquery":jquery})

def logoutfunc(request):
    logout(request)
    return homeview(request)