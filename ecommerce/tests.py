from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import User, Category, Product, Order
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.

class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user_data = {'name': 'Test User', 'email': 'test@example.com', 'phone': '1234567890'}
        self.user = User.objects.create(**self.user_data)
        self.client = APIClient()

    def test_list_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_user(self):
        url = reverse('user-list')
        data = {'name': 'Another User', 'email': 'another@example.com', 'phone': '0987654321'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

class CategoryAPITestCase(APITestCase):
    def setUp(self):
        self.category_data = {'name': 'Electronics', 'description': 'Electronic items'}
        self.category = Category.objects.create(**self.category_data)
        self.client = APIClient()

    def test_list_categories(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_category(self):
        url = reverse('category-list')
        data = {'name': 'Books', 'description': 'All kinds of books'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics', description='Electronic items')
        self.product_data = {
            'name': 'Laptop',
            'description': 'A powerful laptop',
            'price': '999.99',
            'category': self.category
        }
        self.product = Product.objects.create(**self.product_data)
        self.client = APIClient()

    def test_list_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_product(self):
        url = reverse('product-list')
        data = {
            'name': 'Smartphone',
            'description': 'A smart phone',
            'price': '499.99',
            'category': self.category.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

