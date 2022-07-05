from django.shortcuts import render
from store.models.products import Products

def available_view(request):
    books = Products.objects.all()
    return render(request,'available_books.html',{'books':books})