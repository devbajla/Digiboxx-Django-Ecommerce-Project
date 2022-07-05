from django.shortcuts import render
from store.models.orders import Orders
from store.models.user import Users, get_user_by_email

def history_view(request):
    user_email = request.session['user']
    user = get_user_by_email(user_email)

    orders = Orders.objects.filter(user = user)
    return render(request,'history.html',{'orders':orders})