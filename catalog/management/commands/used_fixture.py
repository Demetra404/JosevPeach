from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Add test data from fixture'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('было добавление'))