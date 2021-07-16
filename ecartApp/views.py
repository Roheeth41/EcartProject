from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import products,carts

# Create your views here.
def home(request):
    user_id=request.user.id
    product_data=products.objects.all()
    user_data=products.objects.filter(carts__user=User.objects.get(id=user_id),carts__status=0)
    return render(request,'ecartApp/home.html',context={'products':product_data,'user_data':user_data})

def product(request,id=None):
    if request.method =='POST':
        user_id=request.POST['user']
        product=carts(user=User.objects.get(id=user_id),id=products.objects.get(id=id),quantity=1,status=0)
        product.save()
        product_data=products.objects.filter(carts__user=User.objects.get(id=user_id),carts__status=0)
        return render(request,'ecartApp/cart.html',{'product':product_data})
    else:
        user_id=request.user.id
        product_data=products.objects.get(id=id)
        user_data=products.objects.filter(carts__user=User.objects.get(id=user_id),carts__status=0)
        return render(request,'ecartApp/product.html',{'product':product_data,'user_data':user_data})

def cart(request,id=None):
    if request.method =='POST':
        return render(request,'ecartApp/home.html')
    else:
        user_id=request.user.id
        product_data=products.objects.filter(carts__user=User.objects.get(id=user_id),carts__status=0)
        return render(request,'ecartApp/cart.html',{'product':product_data})

def remove(request,id):
    if request.method=='POST':
        user_id=request.user.id
        product_to_be_deleted=carts.objects.filter(id=id)
        product_to_be_deleted.delete()
        product_data=products.objects.filter(carts__user=User.objects.get(id=user_id),carts__status=0)
        return render(request,'ecartApp/cart.html',{'product':product_data})
    else:
        user_id=request.user.id
        product_data=products.objects.filter(carts__user=User.objects.get(id=user_id),carts__status=0)
        return render(request,'ecartApp/cart.html',{'product':product_data})

def buy(request,id=None):
    if request.method=='POST':
        counter=request.POST['quantity']
        user_id=request.user.id
        product_to_be_ordered=carts.objects.get(id=id)
        product_to_be_ordered.status=1
        product_to_be_ordered.quantity=counter
        product_to_be_ordered.save()
        product_data=products.objects.filter(carts__user=User.objects.get(id=user_id),carts__status=1).all()
        cart_data=carts.objects.filter(user=User.objects.get(id=user_id),status=1).all()
        user_data=products.objects.filter(carts__user=User.objects.get(id=user_id),carts__status=0)
        final_dict=dict()
        final_list=list()
        for product in product_data:
            for item in cart_data:
                if product.id == item.id_id:
                    final_dict['id']=product.id
                    final_dict['name']=product.name
                    final_dict['image']=product.image
                    final_dict['price']=product.price
                    final_dict['quantity']=item.quantity
                    final_list.append(final_dict.copy())      
        return render(request,'ecartApp/order.html',{'product':final_list,'user_data':user_data})
    else:
        user_id=request.user.id
        product_data=products.objects.filter(carts__user=User.objects.get(id=user_id),carts__status=1).all()
        cart_data=carts.objects.filter(user=User.objects.get(id=user_id),status=1).all()
        user_data=products.objects.filter(carts__user=User.objects.get(id=user_id),carts__status=0)
        final_dict=dict()
        final_list=list()
        for product in product_data:
            for item in cart_data:
                if product.id == item.id_id:
                    final_dict['id']=product.id
                    final_dict['name']=product.name
                    final_dict['image']=product.image
                    final_dict['price']=product.price
                    final_dict['quantity']=item.quantity
                    final_list.append(final_dict.copy())      
        return render(request,'ecartApp/order.html',{'product':final_list,'user_data':user_data})

def search(request):
    search_word=request.GET['search']
    user_id=request.user.id
    user_data=products.objects.filter(carts__user=User.objects.get(id=user_id),carts__status=0)
    result=products.objects.filter(name__contains=search_word)
    return render(request,'ecartApp/home.html',{'products':result,'user_data':user_data})
    