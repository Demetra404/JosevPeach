from django.urls import path

#from myproject.myproject.urls import urlpatterns
from . import views
from .views import ProductDetailView, ContactsListView, HomeListView

app_name = 'catalog'

urlpatterns = [
    path('home/', HomeListView.as_view(), name='products'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    #path('product_info/<int:product_id>', views.product_info, name='product_info')
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]