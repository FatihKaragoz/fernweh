from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout


def homeview(request):
    return render(request,'home.html')


def browseview(request):
    return render(request,'browse.html')


def aboutview(request):
    return render(request,'about.html')


def contactview(request):
    return render(request,'contact.html')



