from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homefun(request):
    return render (request,'home.html')


def loginfun(request):
    return render (request,'login.html')


def forgetpasfun(request):
    return render (request,'forgetpass.html')


def resetpasfun(request):
    return render (request,'restpass.html')


def adminhomefun(request):
    return render (request,'admindashboard.html')


def signupfun(request):
    return render (request,'signup.html')

def creatorfun(request):
    return render (request,'creator.html')

def viewerfun(request):
    return render (request,'viewers.html')


