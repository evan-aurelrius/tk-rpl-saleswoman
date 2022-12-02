from django.test import TestCase

from .models import MockSales, Client


class SalesTestCase(TestCase):
    def setUp(self):
        MockSales.objects.create(username='test_sales')
        Client.objects.create(name='test_client1',
                              information='test_information1',
                              sales=MockSales.objects.get(username='test_sales')
                              )

    def test_sales(self):
        sales = MockSales.objects.get(username='test_sales')
        self.assertEqual(sales.username, 'test_sales')
        self.assertEqual(sales.clients.count(), 1)
        self.assertEqual(sales.clients.get(name='test_client1').information, 'test_information1')

    def test_create_client(self):
        sales = MockSales.objects.get(username='test_sales')
        sales.create_client('test_client2', 'test_information2')
        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(Client.objects.get(name='test_client2').information, 'test_information2')
        self.assertEqual(Client.objects.get(name='test_client2').sales.username, 'test_sales')
