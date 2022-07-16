from random import choice, choices
from django.db import models

from django import forms


    
class Question(models.Model):
    choices_are = (
        ('Asia'),
        ('Africa'),
        ('NorthAmerica'),
        ('Antarctica'),
        ('Europe'),
        ('Australia')
    )

class Continent(models.Model):
    choices_are = (
        ('Asia', 'Asia'),
        ('Africa', 'Africa'),
        ('NorthAmerica', 'NorthAmerica'),
        ('Antarctica', 'Antarctica'),
        ('Europe', 'Europe'),
        ('Australia','Australia')
    )
    continents_field = models.CharField(max_length =100, choices = choices_are, default="Asia")


# class Choice(models.Model):
#     question = models.ForeignKey(FirstQuestion, on_delete=models.CASCADE)
