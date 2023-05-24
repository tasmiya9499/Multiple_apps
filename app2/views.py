from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def app2(request):
    return HttpResponse('<h1><marquee>welcome to app2</marquee></h1>')
def awais(request):
    return render(request,'app2htmlpages.html')