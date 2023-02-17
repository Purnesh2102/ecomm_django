from django.shortcuts import render, redirect
from products.models import Product
from accounts.models import *
from django.http import HttpResponseRedirect
# Create your views here.

def get_product(request, slug):
    try:
        
        products = Product.objects.get(product_slug = slug)
        
        context = {
            'products' : products,
            'all_products' : Product.objects.all()
        }
        
        return render(request, 'product/products.html', context)
          
    except Exception as e:
        print(e)
        
