from django.urls import path

#from myproject.myproject.urls import urlpatterns
from . import views
from .views import ProductDetailView, ContactsListView, HomeListView, ProductCreateView, ProductUpdateView, ProductDeleteView, UnpublishProductView

app_name = 'catalog'

urlpatterns = [
    path('home/', HomeListView.as_view(), name='products'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    #path('product_info/<int:product_id>', views.product_info, name='product_info')
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('products/unpublish/<int:pk>', UnpublishProductView.as_view(), name='product_unpublish')

]