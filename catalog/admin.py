from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =  ('id', 'name_category')
    search_fields = ('name_category', 'description_category')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'category_product', 'price_product')
    list_filter = ('category_product',)
    search_fields = ('name_product', 'description_product')