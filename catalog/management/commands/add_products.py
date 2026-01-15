from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Add test products'

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name_category='Оперативная память', description_category='драгоценность')
        products = [
            {'name_products':'Pioneer', 'description_product':'viper venom ddr5', 'category_product':category, 'price_product':1000000},
            {'name_products':'Kingston', 'description_product':'перепаянная и разогнанная ddr4', 'category_product':category, 'price_product':10000},
        ]
        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'yes {product.name_product}'))
            else:
                self.stdout.write(self.style.WARNING(f'no {product.name_product}'))