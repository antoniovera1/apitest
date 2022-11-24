from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


class StatusNameTest(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

        self.client = Client()

    def setUp(self) -> None:
        pass

    def test_statusname(self):
        # Get API response
        response = self.client.get(reverse('product-status'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, {
            1: "Active", 
            0: 'Inactive',
        })