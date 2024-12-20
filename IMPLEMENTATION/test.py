# unitests.py
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Category

class ProductAPITests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            name='Laptop',
            price=999.99,
            description='A high-performance laptop.',
            category=self.category
        )

    def test_product_list(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_search(self):
        response = self.client.get('/products/?name=Laptop')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Laptop')

    def test_category_filter(self):
        response = self.client.get('/products/?category=Electronics')
        self.assertEqual(len(response.data), 1)