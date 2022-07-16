from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def login(request):
    return render(request, 'login.html', {})

def continents(request):
    return render(request, 'continents.html', {})

    
# def index(request):
#     return HttpResponse("Hello, world. You're at the couintries index.")
