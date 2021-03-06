# from random import choice, choices
# from random import choice, choices
from pyexpat import model
from django.db import models

from django import forms

class HolidayRef(models.Model):
    ref = models.IntegerField()
    


class Continent(models.Model):
    continents_field = models.CharField(max_length =100)
    ref = models.ManyToManyField(HolidayRef)
    
    def __str__(self):
        return self.continents_field

class AfricaCountries(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)

    def __str__(self):
        return self.countries

class AustraliaCountries(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)


    def __str__(self):
        return self.countries

class AntarcticaCountries(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)


    def __str__(self):
        return self.countries

class NorthAmericaCountries(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)


    def __str__(self):
        return self.countries


class EuropeCountries(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)

    def __str__(self):
        return self.countries


class AsiaCountries(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)

class TypeHoliday(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    type_hol = models.CharField(max_length =100)
    temp = models.CharField(max_length =100)

    def __str__(self):
        return (f'types is hoildays {self.type_hol} ')


class Holiday(models.Model):
    ref = models.ManyToManyField(HolidayRef)
    continent = models.ManyToManyField(Continent)
    # type = models.ManyToManyField(TypeHol)
    HotelName = models.CharField(max_length =100)
    Area = models.CharField(max_length =100)
    StarRating = models.CharField(max_length =100)
    Location = models.CharField(max_length =100)
    PricePerPerNight = models.CharField(max_length =100)
    
    def __str__(self):
        return(f"{self.HotelName}, {self.Area}, {self.Location}, {self.PricePerPerNight}")