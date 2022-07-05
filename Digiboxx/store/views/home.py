
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

def home_view(request):

    if 'user' in request.session.keys():
        del request.session['user']
        
    return render(request,'home.html')