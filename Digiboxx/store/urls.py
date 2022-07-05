
from django.urls import path
from store.views.home import home_view
from store.views.create import create_view
from store.views.log_in import log_view
from store.views.landing import landing_view
from store.views.return_book import return_view
from store.views.available_books import available_view
from store.views.add_book import add_view
from store.views.history import history_view

urlpatterns = [
    path('',home_view, name= 'home'),
    path('create', create_view, name ='create'),
    path('login', log_view, name ='log_in'),
    path('landing', landing_view, name ='landing'),
    path('return_book', return_view, name ='return_book'),
    path('available_books', available_view, name= 'available_books'),
    path('add_book/<int:id>', add_view, name= 'add_book'), 
    path('history', history_view, name= 'history'),
]
