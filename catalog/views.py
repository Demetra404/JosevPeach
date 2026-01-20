from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView

from .models import Product, Category

# Create your views here.

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'
class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'home'

class ContactsListView(ListView):
    model = Category # как заглушка
    template_name = 'catalog/contacts.html'
    context_object_name = 'contacts'
#def contacts_view(request):
    #return render(request, 'catalog/contacts.html')
