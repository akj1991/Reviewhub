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
    return render (request,'resetpass.html')

def adminhomefun(request):
    return render (request,'admindashboard.html')

def signupfun(request):
    return render (request,'signup.html')

def creatorfun(request):
    return render (request,'creator.html')

def viewerfun(request):
    return render (request,'viewers.html')

def reportsfun(request):
    return render (request,'reports.html')

def requestsfun(request):
    return render (request,'Requests.html')

def settingsfun(request):
    return render (request,'settings.html')

def uploadvideofun(request):
    return render (request,'uploadedvideos.html')

def creloginfun(request):
    return render (request,'creatorLogin.html')

def viewerloginfun(request):
    return render (request,'viewerLogin.html')

def creatorforpassfun(request):
    return render (request,'creatorforgetpass.html')

def creatorrestpassfun(request):
    return render (request,'creatorresetpass.html')

def viewerforpassfun(request):
    return render (request,'viewerforgetpass.html')

def viewerrestpassfun(request):
    return render (request,'viewerresetpass.html')


