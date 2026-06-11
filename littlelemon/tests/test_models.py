from django.test import TestCase

from restaurant.models import Menu


class MenuTest(TestCase):
    def test_create_menu_item(self):
        item = Menu.objects.create(title='Pizza', price=9.99, inventory=10)
        self.assertEqual(str(item), 'Pizza : 9.99')