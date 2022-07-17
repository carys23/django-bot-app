# from random import choice, choices
from pyexpat import model
from django.db import models

from django import forms



class Holiday(models.Model):
    HotelName = models.CharField(max_length =100)
    Area = models.CharField(max_length =100)
    StarRating = models.CharField(max_length =100)
    Location = models.CharField(max_length =100)
    PricePerPerNight = models.CharField(max_length =100)
    
    def __str__(self):
        return(f"{self.HotelName}, {self.Area},{self.Continent}, {self.Country}, {self.Category}, {self.StarRating},{self.TempRating}, {self.Location}, {self.PricePerPerNight}")


class Continent(models.Model):
    continents_field = models.CharField(max_length =100)
    

    def __str__(self):
        return self.continents_field


class AfricaCountries(models.Model):
    countries = models.CharField(max_length =100)
    continent = models.ManyToManyField(Continent)

    def __str__(self):
        return self.countries

class AustraliaCountries(models.Model):
    countries = models.CharField(max_length =100)
    continent = models.ManyToManyField(Continent)

    def __str__(self):
        return self.countries

class AntarcticaCountries(models.Model):
    countries = models.CharField(max_length =100)
    continent = models.ManyToManyField(Continent)

    def __str__(self):
        return self.countries

class NorthAmericaCountries(models.Model):
    countries = models.CharField(max_length =100)
    continent = models.ManyToManyField(Continent)

    def __str__(self):
        return self.countries


class EuropeCountries(models.Model):
    countries = models.CharField(max_length =100)
    continent = models.ManyToManyField(Continent)
    

    def __str__(self):
        return self.countries


class AsiaCountries(models.Model):
    countries = models.CharField(max_length =100)
    continent = models.ManyToManyField(Continent)

    def __str__(self):
        return self.countries

class TypeHoliday(models.Model):
    type_hol = models.CharField(max_length =100)
    holiday_details = models.ManyToManyField(Holiday)

    def __str__(self):
        return (f'types is hoildays {self.type_hol} ')

class Temp(models.Model):
    holiday = models.ManyToManyField(Holiday)
    temp = models.CharField(max_length =100)

    def __str__(self):
        return (f'types is hoildays {self.temp} ')

# class Result(models.Model):
#     result = models.ManyToManyField(Holiday related_name='holidays')
#     type = models.ManyToManyField(Holiday related_name='person2persons')