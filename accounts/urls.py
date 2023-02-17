from django.urls import path , include
from accounts.views import login_page, registration_page, activation_mail, cart, add_to_cart, remove_cart, paymentSuccess

# from accounts.views import registration_page
urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', registration_page, name='registration'),
    path('activate/<email_token>/', activation_mail, name='activation_mail'),
    path('cart/', cart, name='cart'),
    path('add-to-cart/<uid>/', add_to_cart, name='add_to_cart'),  
    path('remove-cart/<uid>/', remove_cart, name='remove_cart'),
    path('success/', paymentSuccess, name='success'),
]