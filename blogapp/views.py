from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # return HttpResponse('<h1>About</h1>')
    return render(request,'about.html')

def homepage(request):
    # return HttpResponse('<h1>HomePage</h1>')
    return render(request,'homepage.html')
