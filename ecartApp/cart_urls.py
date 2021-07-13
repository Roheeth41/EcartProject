from django.contrib import admin
from django.urls import path,include
from ecartApp import views
import authentication

urlpatterns = [
    path('', views.cart,name='cart'),
    path('<int:id>', views.cart,name='cart_dynamic')
]
