import email
from django.shortcuts import render,HttpResponse,redirect
from store.models.user import Users, get_user_by_email
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


@csrf_exempt
def log_view(request):
    if request.method == 'POST':
        postData = request.POST
        user = get_user_by_email(postData['email'])
        password_in = postData['password']
        email_in = postData['email']

        if user:
            if password_in == user.password:
                request.session['user'] = user.email  #'user' session maps to user email
                return redirect('landing')
            else:
                messages.success(request, "Wrong password entered")
                return render(request,'log_in.html')
        else:
            messages.success(request, "Wrong email entered")
            return render(request,'log_in.html')
            
    else:
        return render(request,'log_in.html')
    