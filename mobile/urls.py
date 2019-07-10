from django.urls import path
from .views import Home, About, Products

urlpatterns = [
    path('', Home, name='mobile-home'),
    path('about/', About, name='mobile-about'),
    path('products/', Products, name='mobile-products'),
]
