from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, EMS
# Create your views here.

def Home(request):
	#return HttpResponse('<h1>Hello World</h1>')
	allmobile = Product.objects.all()
	#context = {'phonelist':['I Phone XI','Huawei','Samsung','Oppo']}
	context = {'phonelist':allmobile}
	return render(request, 'mobile/home.html', context)

def About(request):
	#return HttpResponse('<h1>About Us</h1>')
	return render(request, 'mobile/about.html')

def Products(request):
	#return HttpResponse('<h1>Product Page</h1>')
	return render(request, 'mobile/products.html')