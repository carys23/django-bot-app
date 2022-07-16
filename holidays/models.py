# from random import choice, choices
from django.db import models

from django import forms


    
# class Question(models.Model):
#     choices_are = (
#         ('Asia'),
#         ('Africa'),
#         ('NorthAmerica'),
#         ('Antarctica'),
#         ('Europe'),
#         ('Australia')
#     )

# class Continent(models.Model):
#     choices_are = (
#         ('Asia', 'Asia'),
#         ('Africa', 'Africa'),
#         ('NorthAmerica', 'NorthAmerica'),
#         ('Antarctica', 'Antarctica'),
#         ('Europe', 'Europe'),
#         ('Australia','Australia')
#     )
#     continents_field = models.CharField(max_length =100, choices = choices_are, default="Asia")
class Holiday(models.Model):
    hoilday_ref = models.CharField(max_length =100)
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
        return(f"{self.hoilday_ref} ,{self.HotelName}, {self.Area},{self.Continent}, {self.Country}, {self.Category}, {self.StarRating},{self.TempRating}, {self.Location}, {self.PricePerPerNight}")

class Continent(models.Model):
    continents_field = models.ForeignKey(Holiday, on_delete=models.CASCADE)
    def __str__(self):
        return(f"{self.continents_field}")

# class Countries(models.Model):
#     continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
#     countries = models.CharField(max_length =100)
#     def __str__(self):
#         return(f"{self.continent}, {self.countries}")

# class Category(models.Model):
#     countries = models.ForeignKey(Countries, on_delete=models.CASCADE)
#     category = models.CharField(max_length =100)

# class Type(models.Model):
#     type = models.ForeignKey(Category, on_delete=models.CASCADE)
 