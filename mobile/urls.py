from django.urls import path
from .views import Home, About, Products, Emss, QuestionsForm

urlpatterns = [
    path('', Home, name='mobile-home'),
    path('about/', About, name='mobile-about'),
    path('products/', Products, name='mobile-products'),
    path('emss/', Emss, name='mobile-emss'),
    path('questions/', QuestionsForm, name='mobile-qa'),
]
