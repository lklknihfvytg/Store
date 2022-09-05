from django.shortcuts import render
from shop.models import Product

def index(request):
	products = Product.objects.order_by('price')[:4]
	deal = Product.objects.get(id=2)
	return render(request, 'index.html', {'products': products, 'deal': deal})


def about(request):
	return render(request, 'about.html')


def contact(request):
	return render(request, 'contact.html')
