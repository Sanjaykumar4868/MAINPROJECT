from django.shortcuts import render,redirect
from store.models import Product



def home(request):
    return render(request,'App/home.html')



def productpage(request):
    products = Product.objects.filter(status = Product.ACTIVE)[0:6]

    return render(request,'App/products.html',{
        'products':products
    })