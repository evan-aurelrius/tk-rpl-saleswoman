from django.test import TestCase

from clients.models import Client
from account.models import Sales, AdminUser


class ClientTestCase(TestCase):
    def setUp(self):
        self.admin = AdminUser.objects.create(
            full_name='admin1',
            email='admin1@admin.com',
            password='admin1',
            role='ADMIN'
        )

        self.sales = Sales.objects.create(
            full_name='sales1',
            email='sales1@sales.com',
            password='sales1',
            role='SALES',
            created_account=self.admin
        )

        self.client = Client.objects.create(
            name='client1',
            information='info1',
            sales=self.sales
        )

    def test_client(self):
        client = Client.objects.get(name=self.client.name)
        self.assertEqual(client.name, self.client.name)
        self.assertEqual(client.information, self.client.information)
        self.assertEqual(client.sales, self.sales)

    def test_client_str(self):
        self.assertEqual(str(self.client), self.client.name)
