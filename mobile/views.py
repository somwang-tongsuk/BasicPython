from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, EMS
from .forms import QA
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

def Emss(request):
	allems = EMS.objects.all()
	#context= {'emslist':allems, 'title': vulue}
	context= {'emslist':allems}
	return render(request, 'mobile/ems.html', context)

def QuestionsForm(request):
	msg = "error"
	if request.method == 'POST':
		form = QA(request.POST)
		if form.is_valid():
			form.save()
			print('Submit Complete')
			msg = 'Submit Complete'

	form = QA()
	return render(request, 'mobile/form.html',{'forms':form, 'msg':msg})