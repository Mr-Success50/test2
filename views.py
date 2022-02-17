from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
global glob
glob = {"u": "Go 1,000"}

def home(request):
    return render(request,'home.html', glob)

def add(request):
    return render(request, "result.html")  