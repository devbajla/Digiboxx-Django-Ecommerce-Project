
from django.shortcuts import redirect
from store.models.user import Users, get_user_by_email
from store.models.products import Products
from store.models.orders import Orders

def return_view(request):
    #update users
    user_email = request.session['user']
    user = get_user_by_email(user_email)
    user.status = False #user no longer has a book
    user.save()

    #update products
    book_name = request.session['returned_book']
    book = Products.objects.get(book = book_name)
    book.stock += 1
    if book.stock > 0:
        book.status = True
    book.save()

    #update orders
    order = Orders.objects.get(user = user, product = book, status = True)
    order.status = False
    order.save()

    del request.session['returned_book']

    return redirect('landing')