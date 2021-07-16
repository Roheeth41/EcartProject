from django.contrib import admin
from django.urls import path,include
from ecartApp import views 
import authentication

urlpatterns = [
    path('', views.home,name='app'),
    path('home', authentication.views.home,name='home'),
    path('logout', authentication.views.logout,name='logout'),
    path('cart', views.cart,name='cart'),
    path('product/',include('ecartApp.product_urls')),
    path('remove/', include('ecartApp.remove_urls')),
    path('buy/', include('ecartApp.buy_urls')),
    path('order/', views.buy,name='order'),
    path('search', views.search,name='search'),
    path('order/logout', authentication.views.logout,name='logout'),
    path('order/search',views.search,name='search'),
    path('search', views.search,name='search'),
]
