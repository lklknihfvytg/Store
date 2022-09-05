from django.shortcuts import render
from django.views.generic import ListView, DetailView
from shop.models import Product

class ProductsListView(ListView):
	model = Product
	template_name = 'shop-page.html'


class ProductsDetailView(DetailView):
	model = Product
	template_name = 'product-details.html'

