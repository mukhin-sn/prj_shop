from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'pk': 1, 'name': 'automobile', 'description': 'Cars and trucks'},
            {'pk': 2, 'name': 'motorbike', 'description': 'Sports motorcycles and chopper'},
            {'pk': 3, 'name': 'bike', 'description': 'Sports, city and mountain bikes'},
        ]

        product_list = [
            {'name': 'Largus', 'description': 'Auto VAZ - универсал', 'category_id': 1, 'price_for_one': 1600000},
            {'name': 'Amarok', 'description': 'Volkswagen - пикап', 'category_id': 1, 'price_for_one': 6500000},
            {'name': 'Cross Bones', 'description': 'Harley-Davidson', 'category_id': 2, 'price_for_one': 1400000},
            {'name': 'NT1100', 'description': 'Honda', 'category_id': 2, 'price_for_one': 2530000},
            {'name': 'Avalanche 1.0', 'description': 'GT', 'category_id': 3, 'price_for_one': 52000},
            {'name': 'LABOMBA PRO', 'description': 'GT', 'category_id': 3, 'price_for_one': 120000},
            {'name': 'Note', 'description': 'Nissan', 'category_id': 1, 'price_for_one': 2200000},
        ]

        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_create = []
        product_for_create = []

        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
