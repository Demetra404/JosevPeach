from .models import Product, Category

class ProductServiceNotWork:

    @staticmethod
    def products_in_category(category):
        products = Product.objects.filter(category_product = category)
        list_products = []
        #if not product.exist():
            #return None
        products_in = list_products.append(product.name_product for product in products)
        return products_in

class ProductService:

    @staticmethod
    def get_products_in_category(category_id):
        products_in_category = Product.objects.filter(category_productc_id=category_id)
        if not products_in_category.exists():
            return None
        return products_in_category