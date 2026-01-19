from django.shortcuts import render
from .models import Product

# Create your views here.
def home_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context=context)
def contacts_view(request):
    return render(request, 'catalog/contacts.html')
def product_info(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'catalog/product_info.html', context=context)