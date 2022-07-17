# from random import choice, choices
from django.db import models

from django import forms



class Holiday(models.Model):
    HotelName = models.CharField(max_length =100)
    Area = models.CharField(max_length =100)
    Continent = models.CharField(max_length =100)
    Country = models.CharField(max_length =100)
    Category = models.CharField(max_length =100)
    StarRating = models.CharField(max_length =100)
    TempRating = models.CharField(max_length =100)
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

    def __str__(self):
        return self.countries

class AustraliaCountries(models.Model):
    countries = models.CharField(max_length =100)


    def __str__(self):
        return self.countries

class AntarcticaCountries(models.Model):
    countries = models.CharField(max_length =100)

    def __str__(self):
        return self.countries

class NorthAmericaCountries(models.Model):
    countries = models.CharField(max_length =100)

    def __str__(self):
        return self.countries


class EuropeCountries(models.Model):
    countries = models.CharField(max_length =100)
    

    def __str__(self):
        return self.countries


class AsiaCountries(models.Model):
    countries = models.CharField(max_length =100)

    def __str__(self):
        return self.countries

class TypeHoliday(models.Model):
    type_hol = models.CharField(max_length =100)
    # holiday = models.ManyToManyField(Holiday)
    continent = models.ManyToManyField(Holiday)
    def __str__(self):
        return (f'types is hoildays {self.continent} ')
 