from django.shortcuts import redirect
from store.models.user import Users, get_user_by_email
from store.models.products import Products
from store.models.orders import Orders

def add_view(request,id):
    book = Products.objects.get(id = id)
    user_email = request.session['user']
    user = get_user_by_email(user_email)

    #update orders
    order = Orders(user = user, product = book, status = True)
    order.save()

    #update user
    user.status = True 
    user.save()

    #product update
    book.stock -= 1
    if book.stock < 1:
        book.status = False
    book.save()

    return redirect('landing')