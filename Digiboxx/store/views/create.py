from django.shortcuts import render, redirect
from datetime import datetime
from store.models.user import Users
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here.

@csrf_exempt
def create_view(request):

    if request.method == 'POST':
        postData = request.POST
        now = datetime.now()
        postData = request.POST
        user = Users()
        user.name = postData['name']
        user.mobile = postData['mobile']
        user.email = postData['email']
        user.password = postData['password']
        user.created_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
        user.lastmodified_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
        user.save()

        messages.success(request, "The employee "+ user.name +" was inserted sucessfully")
        return render(request,"create.html")

    else:
        return render(request,"create.html")
    
