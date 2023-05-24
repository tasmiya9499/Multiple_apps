from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app1(request):
    return HttpResponse('<h1><marquee>welcome to app1</marquee></h1>')
def Tassu(request):
    return render(request,'app1htmlpages.html')
