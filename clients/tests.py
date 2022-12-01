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

    def test_create_view_success(self):
        response = self.client.post('/clients/create-client/',
                                    {'name': 'test_client3',
                                     'information': 'test_information3',
                                     'sales': MockSales.objects.get(username='test_sales').id
                                     })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(Client.objects.get(name='test_client3').information, 'test_information3')
        self.assertEqual(Client.objects.get(name='test_client3').sales.username, 'test_sales')

    def test_create_view_error_no_name(self):
        response = self.client.post('/clients/create-client/',
                                    {'name': '', 'information': 'test_information',
                                     'sales': MockSales.objects.get(username='test_sales').id
                                     })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Client.objects.count(), 1)

    def test_create_view_error_no_information(self):
        response = self.client.post('/clients/create-client/',
                                    {'name': 'test_client', 'information': '',
                                     'sales': MockSales.objects.get(username='test_sales').id
                                     })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Client.objects.count(), 1)

    def test_create_view_error_no_sales(self):
        response = self.client.post('/clients/create-client/',
                                    {'name': 'test_client', 'information': 'test_information', 'sales': ''
                                     })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Client.objects.count(), 1)

    def test_get_details_view(self):
        response = self.client.get('/clients/details/', {'sales_username': 'test_sales',
                                                         'client_name': 'test_client1'
                                                         })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test_client1')
        self.assertContains(response, 'test_information1')

    def test_get_details_view_error_invalid_sales_username(self):
        response = self.client.get('/clients/details/', {'sales_username': 'john_doe',
                                                         'client_name': 'test_client1'
                                                         })
        self.assertEqual(response.status_code, 404)

    def test_get_details_view_error_invalid_client_name(self):
        response = self.client.get('/clients/details/', {'sales_username': 'test_sales',
                                                         'client_name': 'x'
                                                         })
        self.assertEqual(response.status_code, 404)
