from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import Profile
from accounts.models import *
import razorpay
from django.conf import settings


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = email)
        
        if not user.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)
        
        if not user[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)
            
        user = authenticate(username = email, password = password)
        if user:
            login(request, user)
            return redirect('/')
        
    return render(request, 'accounts/login.html')

def registration_page(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = email)
        
        if user.exists():
            messages.warning(request, 'Email is already registered.')
            return HttpResponseRedirect(request.path_info)
        
        user = User.objects.create(first_name = first_name, last_name = last_name, email = email, username = email)
        user.set_password(password)
        user.save()
        
        messages.success(request, 'Email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)
                    
    return render(request, 'accounts/registration.html')

def activation_mail(request, email_token):
    try:
        user = Profile.objects.get(email_token = email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email Token.')
   
def remove_cart(request, uid):
    try:
        cart_item = CartItems.objects.get(uid=uid)
        cart_item.delete()
    except Exception as e:
        print(e)
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
 
def cart(request):
    # cart_obj = None
    cart_obj = Cart.objects.get(is_paid= False, user=request.user)
    # try:
    #     cart_obj = Cart.objects.get(is_paid= False, user=request.user)
    # except Exception as e:
    #     print(e)
    
    # if request.method == 'POST':
    # razorpay integration
    # if cart_obj:
    #     client = razorpay.Client(auth = (settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    #     payment = client.order.create({'amount': cart_obj.get_cart_total()*100, 'currency' : 'INR', 'payment_capture': 1})
    #     cart_obj.razor_pay_order_id = payment['id']
    #     cart_obj.save()
    
    # payment = None
    
    context = {
        'cart': cart_obj,
        # 'payment' : payment,
    }
    
    return render(request, 'accounts/cart.html', context)

def add_to_cart(request, uid):
    variant = request.GET.get('variant')
    product = Product.objects.get(uid=uid)
    user = request.user
    cart , _ = Cart.objects.get_or_create(user=user, is_paid=False)
    
    cart_item = CartItems.objects.create(cart=cart, product=product)
    
    if variant:
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size = variant)
        cart_item.size_variant = size_variant
        cart_item.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def paymentSuccess(request):
    order_id = request.GET.get('order_id')
    cart = Cart.objects.get(razor_pay_order_id = order_id)
    cart.is_paid = True
    cart.save()
    return HttpResponse('Payment Success.')
    



    