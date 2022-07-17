# from random import choice, choices
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
    continents_field = models.CharField(max_length =100)
    
    def __str__(self):
        return(f"{self.HotelName}, {self.Area}, {self.Location}, {self.PricePerPerNight}")


class Continent(models.Model):
    continents_field = models.CharField(max_length =100)
    
    def __str__(self):
        return self.continents_field


class AfricaCountries(models.Model):
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)
    

    def __str__(self):
        return self.countries

class AustraliaCountries(models.Model):
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)


    def __str__(self):
        return self.countries

class AntarcticaCountries(models.Model):
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)


    def __str__(self):
        return self.countries

class NorthAmericaCountries(models.Model):
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)


    def __str__(self):
        return self.countries


class EuropeCountries(models.Model):
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)

    

    def __str__(self):
        return self.countries


class AsiaCountries(models.Model):
    continent = models.ManyToManyField(Continent)
    countries = models.CharField(max_length =100)

    def __str__(self):
        return (F'Countries are : {self.countries} and continent are {self.continent}')

class TypeHoliday(models.Model):
    type_hol = models.CharField(max_length =100)

    def __str__(self):
        return (f'types is hoildays {self.type_hol} ')

class Temp(models.Model):
    temp = models.CharField(max_length =100)


class Result(models.Model):
    result = models.ManyToManyField(Holiday)
    def __str__(self):
        return (f'types is hoildays {self.result} ')


# # class Type(models.Models):

# class Result(models.Model):
#     result = models.ManyToManyField(Holiday)
#     type = models.ManyToManyField(TypeHoliday)