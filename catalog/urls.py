from django.urls import path

#from myproject.myproject.urls import urlpatterns
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('product_info/<int:product_id>', views.product_info, name='product_info')
]