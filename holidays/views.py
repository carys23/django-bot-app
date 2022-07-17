from typing import Type
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Holiday, Continent , AfricaCountries, AsiaCountries, NorthAmericaCountries, AntarcticaCountries, AustraliaCountries, EuropeCountries, TypeHoliday


def login(request):
    return render(request, 'login.html', {})

def countries(request):
    holiday = {"continent": Continent.objects.all()}
    return render (request, 'countries.html', holiday )

def asia(request):
    holiday = {"countries": AsiaCountries.objects.all()}

    return render (request, 'asia.html', holiday )

def australia(request):
    holiday = {"countries": AustraliaCountries.objects.all()}
    return render(request, 'australia.html', holiday)

def north_america(request):
    holiday = {"countries": NorthAmericaCountries.objects.all()}
    return render(request, 'north_america.html', holiday)

def antarctica(request):
    holiday = {"countries": AntarcticaCountries.objects.all()}
    return render(request, 'antarctica.html', holiday)

def europe(request):
    holiday = {"countries": EuropeCountries.objects.all()}
    return render(request, 'europe.html', holiday)

def africa(request):
    holiday = {"countries": AfricaCountries.objects.all()}

    return render (request, 'africa.html', holiday )

def TypeHoliday(request):
    holiday = {"TypeHoliday": TypeHoliday.objects.all()}
    return render (request, 'hol-type.html', holiday )