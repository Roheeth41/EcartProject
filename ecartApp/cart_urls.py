from django.contrib import admin
from django.urls import path,include
from ecartApp import views
import authentication

urlpatterns = [
    path('', views.cart,name='cart'),
    path('order', views.buy,name='order'),
    path('search', views.search,name='search'),
    path('logout', authentication.views.logout,name='logout'),
    path('<int:id>', views.cart,name='cart_dynamic')
]
