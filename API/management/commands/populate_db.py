import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from API.models import User, Product, Order, OrderItem

class Command(BaseCommand):
    help = 'creates application data'

    def handle(self, *args, **kwargs):
        # get or create superuser
        user = User.objects.filter(username = 'admin').first()
        if not user:
            user = User.objects.create_superuser(username = 'admin', password = 'test')

        products = [
            Product(name="A Scanner Darkley", description=lorem_ipsum.paragraph(), price=Decimal('12.99'), stock=4),
            Product(name="Coffee Machine", description=lorem_ipsum.paragraph(), price=Decimal('72.9'), stock=6),
            Product(name="Velvet Underground & Nico", description=lorem_ipsum.paragraph(), price=Decimal('15.99'), stock=14),
            Product(name="Enter the Wu-tang(36 chambers)", description=lorem_ipsum.paragraph(), price=Decimal('12.99'), stock=7),
            Product(name="Digital Camera", description=lorem_ipsum.paragraph(), price=Decimal('12.99'), stock=4),
            Product(name="Watch", description=lorem_ipsum.paragraph(), price=Decimal('12.99'), stock=0),
        ]

        Product.objects.bulk_create(products)
        products = Product.objects.all()

        for _ in range(3):
            order = Order.objects.create(user=user)
            for product in random.sample(list(products), 2):
                OrderItem.objects.create(
                    order=order, product=product, quantity=random.randint(1,3)
                )