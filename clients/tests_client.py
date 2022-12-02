from django.test import TestCase

from .models import MockSales, Client
from .forms import ClientForm


class ClientTestCase(TestCase):
    def setUp(self):
        MockSales.objects.create(username='test_sales')
        Client.objects.create(name='test_client1',
                              information='test_information1',
                              sales=MockSales.objects.get(username='test_sales')
                              )

    def test_client(self):
        client = Client.objects.get(name='test_client1')
        self.assertEqual(client.name, 'test_client1')
        self.assertEqual(client.information, 'test_information1')
        self.assertEqual(client.sales.username, 'test_sales')

    def test_form(self):
        form = ClientForm({'name': 'test_client2',
                           'information': 'test_information2',
                           'sales': MockSales.objects.get(username='test_sales').id
                           })
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(Client.objects.get(name='test_client2').information, 'test_information2')
        self.assertEqual(Client.objects.get(name='test_client2').sales.username, 'test_sales')
