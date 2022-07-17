from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Holiday, Continent



def login(request):
    return render(request, 'login.html', {})

def countries(request):
    return render(request, 'countries.html', {})

def asia(request):
    return render(request, 'asia.html', {})

def africa(request):
    return render(request, 'africa.html', {})

def australia(request):
    return render(request, 'africa.html', {})

def south_america(request):
    return render(request, 'africa.html', {})

def antarctica(request):
    return render(request, 'africa.html', {})

def europe(request):
    return render(request, 'africa.html', {})

def detail(request, holiday_id):
    holiday = {"holiday": Holiday.objects.get(pk=holiday_id)}
    return render (request, "countries.html" , holiday)


# def index(request):
#     return HttpResponse("Hello, world. You're at the couintries index.")
