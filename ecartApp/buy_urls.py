from django.contrib import admin
from django.urls import path,include
from ecartApp import views
import authentication

urlpatterns = [
    path('', views.buy,name='buy'),
    path('<int:id>', views.buy,name='buy_dynamic'),
    path('logout', authentication.views.logout,name='logout'),
]
