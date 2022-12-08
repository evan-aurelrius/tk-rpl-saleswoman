from django.test import TestCase

from account.models import Sales, AdminUser


class ViewTestCase(TestCase):
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

    def test_create_client_no_login(self):
        response = self.client.post(
            '/clients/create-client/',
            {'name': 'client1', 'information': 'info1'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.sales.clients.count(), 0)

    def test_create_client_no_sales(self):
        self.client.cookies['user'] = self.admin.id
        response = self.client.post(
            '/clients/create-client/',
            {'name': 'client1', 'information': 'info1'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.sales.clients.count(), 0)

    def test_create_client_success(self):
        self.client.cookies['user'] = self.sales.id
        response = self.client.post(
            '/clients/create-client/',
            {'name': 'client1', 'information': 'info1'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['create_code'], 1)
        self.assertEqual(self.sales.clients.count(), 1)

    def test_create_client_fail1(self):
        self.client.cookies['user'] = self.sales.id
        response = self.client.post(
            '/clients/create-client/',
            {'name': '', 'information': 'info1'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['create_code'], 0)
        self.assertEqual(self.sales.clients.count(), 0)

    def test_create_client_fail2(self):
        self.client.cookies['user'] = self.sales.id
        response = self.client.post(
            '/clients/create-client/',
            {'name': 'client1', 'information': ''}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['create_code'], 0)
        self.assertEqual(self.sales.clients.count(), 0)

    def test_create_client_get(self):
        self.client.cookies['user'] = self.sales.id
        response = self.client.get('/clients/create-client/')
        self.assertEqual(response.status_code, 302)

    def test_get_details_no_login(self):
        response = self.client.get('/clients/details/')
        self.assertEqual(response.status_code, 401)

    def test_get_details_no_sales(self):
        self.client.cookies['user'] = self.admin.id
        response = self.client.get('/clients/details/')
        self.assertEqual(response.status_code, 403)

    def test_get_details_success(self):
        self.sales.clients.create(
            name='client1',
            information='info1'
        )
        self.client.cookies['user'] = self.sales.id

        response = self.client.get('/clients/details/', {'client_name': self.sales.clients.first().name})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'client1')
        self.assertContains(response, 'info1')

    def test_get_details_fail(self):
        self.sales.clients.create(
            name='client1',
            information='info1'
        )
        self.client.cookies['user'] = self.sales.id

        response = self.client.get('/clients/details/', {'client_name': 'client2'})
        self.assertEqual(response.status_code, 404)
