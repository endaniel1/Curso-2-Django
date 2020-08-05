from django.shortcuts import render
from .models import Category,Product

# Create your views here.

def myView(request):	
	data = {
		"name":"Enrique",
		"categories": Category.objects.all()
	}
	return render(request,"prueba1.html", data)

def myView2(request):	
	data = {
		"name":"Enrique prueba",
		"products": Product.objects.all()
	}
	return render(request,"prueba2.html", data)