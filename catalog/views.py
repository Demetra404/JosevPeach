from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic import CreateView, DeleteView
from .forms import ProductForm
from .models import Product, Category

# Create your views here.

class ProductCreateView(CreateView):
    model = Product
    form_class =  ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:products')

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
