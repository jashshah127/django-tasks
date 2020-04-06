from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    query = request.GET.get('name')
    message= "Hello World, this is {}".format(query)
   
    context={
        'message':message,
    }
    return HttpResponse("Hello World")
   
   

def hello(request):
    query = request.GET.get('name')
    message= "Hello World, this is jash {}".format(query)
   
    context={
        'message':message,
    }
    return HttpResponse("Hello World jashhhhhh")


def about_us(request):
    query = request.GET.get('name')
    message= "Hello World, this is jash {}".format(query)
   
    context={
        'message':message,
    }
    return HttpResponse("Hello World Kirtan")
    #return render(request, 'world/kirtan.html',context)