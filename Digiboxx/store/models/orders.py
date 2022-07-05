from tkinter import CASCADE
from django.db import models
from unicodedata import name

from store.models.products import Products
from .user import Users

# Create your models here.

class Orders(models.Model):
    user = models.ForeignKey(Users,on_delete= models.CASCADE)
    product = models.ForeignKey(Products,on_delete= models.CASCADE)
    status = models.BooleanField(default= False) #True if book is currently borrowed