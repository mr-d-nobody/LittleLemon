from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        Menu.objects.create(title='Pizza', price=9.99, inventory=10)
        Menu.objects.create(title='Pasta', price=12.50, inventory=5)
        Menu.objects.create(title='Salad', price=7.25, inventory=8)

    def test_getall(self):
        response = self.client.get(reverse('menu-items'))
        self.assertEqual(response.status_code, 200)

        queryset = Menu.objects.all()
        serialized = MenuSerializer(queryset, many=True)
        self.assertEqual(response.data, serialized.data)
