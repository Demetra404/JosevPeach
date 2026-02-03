from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import View
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
#from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic import CreateView, DeleteView
from .forms import ProductForm
from .services import ProductService
from .models import Product, Category

# Create your views here.

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class =  ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products')
    permission_required = 'catalog.change_product'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            return HttpResponseForbidden("Вы не владелец продукта")
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:products')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        is_owner = obj.owner == request.user
        is_moderator = request.user.has_perm('catalog.delete_product')

        if not (is_owner or is_moderator):
            return HttpResponseForbidden("Вы не можете удалить продукт")
        return super().dispatch(request, *args, **kwargs)

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'

class HomeListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'home'

    def get_queryset(self):
        queryset = cache.get('home_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('home_queryset', queryset, 60*15)
        return queryset

class ContactsListView(ListView):
    model = Category # как заглушка
    template_name = 'catalog/contacts.html'
    context_object_name = 'contacts'
#def contacts_view(request):
    #return render(request, 'catalog/contacts.html')
class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав редактирования")

        product.publication_status = False
        product.save()

        return redirect('catalog:product_detail', pk=pk)
'''
class ProductsListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_categories = Category.objects.all()
        dfs = []
        for category in all_categories:
            dfs.append(ProductService.products_in_category(category))
        context['list_products'] = dfs
        return context
'''

class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context['products_in_category'] = ProductService.get_products_in_category(category_id)
        return context



