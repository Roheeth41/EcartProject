from django.contrib import admin
from .models import products,carts

# Register your models here.
admin.site.register(products)
admin.site.register(carts)