import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from product.models import Product
from product.serializers import ProductSerializer


class ProductCreateTest(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

        self.client = Client()

    def setUp(self) -> None:
        self.valid_payload = {
            'name': 'test_product',
            'stock': 14,
            'description': 'This is a valid description',
            'price': 99.28,
        }
        self.invalid_payload = {
            'name': '',
            'stock': 'asdf',
            'description': 234,
            'price': None,
        }

    def test_crete_product(self):
        # Get API response
        response = self.client.post(
            reverse('product-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_crete_invalid_product(self):
        # Get API response
        response = self.client.post(
            reverse('product-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ProductRetrieveTest(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

        self.client = Client()

    def setUp(self) -> None:
        self.test_product = Product.objects.create(
            name='test product',
            status=1,
            stock=50,
            description="description text",
            price=99,
        )

    def test_list_products(self):
        # Get API response
        response = self.client.get(reverse('product-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Get data from db
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        # Make a copy of the data
        response_data = response.data.copy()
        serializer_data = serializer.data.copy()

        # Check all the non changing values
        for product_resp, product_serial in zip(response_data, serializer_data):
            # Remove everchanging values
            product_resp.pop("discount")
            product_resp.pop("final_price")
            product_serial.pop("discount")
            product_serial.pop("final_price")

        self.assertEqual(response_data, serializer_data)

    def test_retrieve_product(self):
        # Get API response
        response = self.client.get(
            reverse('product-detail', kwargs={'pk': self.test_product.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Get data from db
        product = Product.objects.get(pk=self.test_product.pk)
        serializer = ProductSerializer(product)

        # Make a copy of the data
        response_data = response.data.copy()
        serializer_data = serializer.data.copy()

        # Remove everchanging values
        response_data.pop("discount")
        response_data.pop("final_price")
        serializer_data.pop("discount")
        serializer_data.pop("final_price")

        self.assertEqual(response_data, serializer_data)

    def test_retrieve_invalid_product(self):
        response = self.client.get(
            reverse('product-detail', kwargs={'pk': 999_999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ProductUpdateTest(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

        self.client = Client()

    def setUp(self) -> None:
        self.test_product = Product.objects.create(
            name='test product',
            status=1,
            stock=50,
            description="description text",
            price=99.99,
        )

        self.valid_payload = {
            'name': 'test_product',
            'stock': 14,
            'description': 'This is a valid description',
            'price': 99.28,
        }
        self.invalid_payload = {
            'name': '',
            'stock': 'asdf',
            'description': 234,
            'price': None,
        }

    def test_update_product(self):
        # Get API response
        response = self.client.put(
            reverse('product-detail', kwargs={'pk': self.test_product.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_product(self):
        # Get API response
        response = self.client.put(
            reverse('product-detail', kwargs={'pk': self.test_product.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ProductDeleteTest(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

        self.client = Client()

    def setUp(self) -> None:
        self.test_product = Product.objects.create(
            name='test product',
            status=1,
            stock=50,
            description="description text",
            price=99.99,
        )

    def test_delete_product(self):
        # Get API response
        response = self.client.delete(
            reverse('product-detail', kwargs={'pk': self.test_product.pk}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_product(self):
        # Get API response
        response = self.client.delete(
            reverse('product-detail', kwargs={'pk': 999_999}),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
