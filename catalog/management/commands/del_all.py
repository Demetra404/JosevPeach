from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Delete all data'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()