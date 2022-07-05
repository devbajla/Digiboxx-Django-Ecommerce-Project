from django.db import models
from unicodedata import name

# Create your models here.

class Products(models.Model):
    book = models.CharField(max_length=30)
    stock = models.PositiveIntegerField()
    status = models.BooleanField(default= True) #True if book can be borrowed
    sell = models.BooleanField(default= True)