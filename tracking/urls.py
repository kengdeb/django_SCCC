from django.urls import path
#from .views import Home, About, Test1, Search
from .views import *

urlpatterns = [
    path('', Home,name = 'home-page'),
    path('about/',About, name ='about-page'),
    path('test1/',Test1, name = 'test1-page'),
    path('search/',Search, name ='search-page'),
]
