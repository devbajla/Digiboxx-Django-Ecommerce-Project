from decimal import Context
from multiprocessing import context
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from store.models.orders import Orders
from store.models.user import Users, get_user_by_email

def landing_view(request):
    #check status and send to appropriate page
    user_email = request.session['user']
    user = get_user_by_email(user_email)

    if user.status: #If already has a book
        order = Orders.objects.get(user = user, status = True)
        book = order.product
        context = {'book':book}
        request.session['returned_book'] = book.book
        return render(request,'landing_return.html',context)
        
    else: #if does not have a book
        return render(request,'landing.html')


    
    