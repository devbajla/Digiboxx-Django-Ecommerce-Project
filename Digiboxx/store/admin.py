from django.contrib import admin
from .models.user import *
from .models.products import *
from .models.orders import *

# Register your models here.
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Orders)

