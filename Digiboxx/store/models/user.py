from django.db import models
from unicodedata import name

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length= 15)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    created_datetime = models.DateTimeField(max_length=50)
    lastmodified_datetime = models.DateTimeField(max_length=50)
    status = models.BooleanField(default= False) #Does user have a book already


def get_user_by_email(email):
    try:
        return Users.objects.get(email= email)
    except:
        return False