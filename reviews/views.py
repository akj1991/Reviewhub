from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def fun1(request):
    return render (request,'home.html')
