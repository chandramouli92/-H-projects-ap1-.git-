from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

# Create your views here.
def index(request):
    return HttpResponse("<h1>wlcome to myapp</h1>") 
def home(request):
    return render(request,"sample.html",{'name':"chandu"})
def fact(request,n):
    n=int(n)
    return HttpResponse("<h4>the factorial of {}</h4>".format(factorial(n)))
