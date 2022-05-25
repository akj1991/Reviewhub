from random import random
from django.shortcuts import redirect, render
from . models import *


# from reviews.models import Registration

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
    if request.method=='POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        nationality = request.POST['nationality']
        age = request.POST['age']
        password = request.POST['password']
        repassword = request.POST['repassword']
        details = Registration(fullname=fullname,username=username,email=email,phone=phone,nationality=nationality,age=age,password=password,repassword=repassword)
        details.save()
        return redirect("creator")
    return render (request,'registration.html')

def creatorfun(request):
    infodetails = Registration.objects.all()
    return render (request,'creator.html',{'info': infodetails})

def deletefun(request,id):
    Registration.objects.get(id=id).delete()
    return redirect ('creator')

def updatefun(request,id):
    updatedata = ''
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        nationality = request.POST['nationality']
        age = request.POST['age']
        password = request.POST['password']
        repassword = request.POST['repassword']
        Registration.objects.filter(id=id).update(fullname=fullname,username=username,email=email,phone=phone,nationality=nationality,age=age,password=password,repassword=repassword)
        return redirect ('creator')
    else:
        updatedata = Registration.objects.get(id=id)
    return render (request,'updateform.html',{'update':updatedata} )

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


