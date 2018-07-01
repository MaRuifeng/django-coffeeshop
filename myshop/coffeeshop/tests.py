from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Category, DrinkType, Drink, Size, Order

# TODO The test suites and cases need to be greatly expanded for better coverage. - Ruifeng Ma, Jun-30th

def create_order():
    category = Category.objects.create(name="Coffee")
    size = Size.objects.create(name="Tall")
    drink_type = DrinkType.objects.create(name="Espresso", category=category)
    drink = Drink.objects.create(price=1.25, drink_type=drink_type, size=size)
    return Order.objects.create(quantity=2, drink=drink, ordered_at=timezone.now())

class OrderModelTests(TestCase):
    def test_total_sales(self):
        """
        total_sales should be equal to all prices summed up
        """
        order = create_order()
        self.assertEquals(Order.total_sales(), 2.5)

class OrderListViewTests(TestCase):
    def test_no_order(self):
        response = self.client.get(reverse('coffeeshop:order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['order_list'], [])

    def test_single_order(self):
        order = create_order()
        response = self.client.get(reverse('coffeeshop:order_list'))
        self.assertQuerysetEqual(
            response.context['order_list'],
            [repr(order)]
        )
