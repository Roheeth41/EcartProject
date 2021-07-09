from django.contrib import admin
from django.urls import path,include
from productPage import views

urlpatterns = [
    path('', views.product,name='product'),
    path('1',views.product,name='product1')
]
