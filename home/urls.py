from django.urls import path , include
from home.views import index
# from accounts.views import registration_page

urlpatterns = [
    path('', index, name='index'),
]