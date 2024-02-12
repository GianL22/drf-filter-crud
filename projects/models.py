from django.db import models
from django.utils import timezone
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    created_at = models.DateField( auto_now_add=True) 


class Product(models.Model):

    PRODUCT_CATEGORIES ={
        'SHOES': 'SHOES', 
        'SHIRTS': 'SHIRTS',
        'PANTS': 'PANTS',
        'HATS': 'HATS'
    } 
    PRODUCT_SIZE = {
        'S': 'S',
        'M': 'M',
        'L': 'L',
        'XL': 'XL',
        'XXL': 'XXL',
    }
    COLORS = {
        'RED' : 'RD' ,
        'BLUE' : 'BE',
        'WHITE' : 'WE',
        'BLACK' : 'BK',
        'GREEN' : 'GN',
        'ORANGE' : 'OE'
    }

    title = models.CharField(max_length = 50)
    description = models.TextField(blank = True)
    category = models.CharField(max_length = 10 , choices = PRODUCT_CATEGORIES)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    discount = models.PositiveSmallIntegerField(null = True)
    color    = models.CharField(max_length = 10, choices = COLORS)
    size     = models.CharField(max_length = 4, choices = PRODUCT_SIZE)
    published_at = models.DateField(auto_now_add = True)