from django.urls import path , include
from products.views import get_product

# from accounts.views import registration_page

urlpatterns = [
    path('<slug>/', get_product, name='get_product'),
]