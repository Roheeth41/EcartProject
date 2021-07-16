from django.contrib import admin
from django.urls import path,include
from ecartApp import views 
import authentication

urlpatterns = [
    path('', views.product,name='product'),
    path('home', authentication.views.home,name='home'),
    path('logout', authentication.views.logout,name='logout'),
    path('cart/', include('ecartApp.cart_urls')),
    path('order', views.buy,name='order'),
    path('<int:id>', views.product,name='product_dynamic'),
]
