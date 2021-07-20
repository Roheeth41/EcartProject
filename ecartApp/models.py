from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class products(models.Model):
    name=models.CharField(max_length=100,db_column='Name')
    price=models.IntegerField(db_column='Price')
    description=models.TextField(max_length=25,db_column='Description')
    image=models.ImageField(upload_to='',db_column='Image')
    long_description=models.TextField(db_column='Long Description')

    def __str__(self):
        return self.name

class carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,db_column='User')
    id=models.ForeignKey(products,on_delete=models.DO_NOTHING,db_column='id',primary_key=True)
    quantity=models.IntegerField(db_column='Quantity')
    status=models.BooleanField(db_column='Status')

    def __str__(self):
        return f"Cart_{ self.user }"