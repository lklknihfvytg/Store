from django.views.generic import TemplateView
from django.urls import path, include
from shop import views

app_name = 'shop'

urlpatterns = [
	path('', views.ProductsListView.as_view(), name='shop'),
	path('cart/', TemplateView.as_view(template_name='cart.html'), name='cart'),
	path('detail/<int:pk>', views.ProductsDetailView.as_view(), name='shop_detail'),
]