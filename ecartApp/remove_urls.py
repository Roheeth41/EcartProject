from django.contrib import admin
from django.urls import path,include
from ecartApp import views
import authentication

urlpatterns = [
    path('', views.remove,name='remove'),
    path('<int:id>', views.remove,name='remove_dynamic')
]
