from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import proyect

# Create your views here.
def hello(request, username):
    return HttpResponse("<h1>hello %s<h1>"%username)


def about(request):
    return HttpResponse("<h1>about<h1>")

def index(request):
    return HttpResponse("index")    

def proyects(request):
    proyects= list(proyect.objects.values())
    return JsonResponse(proyects, safe=False)  

def products(request):
    return HttpResponse("products")  