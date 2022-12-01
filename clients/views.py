import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from clients.forms import ClientForm
from clients.models import MockSales, Client


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['create_code'] = 1  # 1 = success
            return redirect('client_index')
        else:
            request.session['create_code'] = 0  # 0 = error
            return redirect('client_index')

    return redirect('client_index')


def index(request):
    form = ClientForm()
    create_code = -1
    if 'create_code' in request.session:
        create_code = request.session['create_code']
        del request.session['create_code']

    context = {
        'form': form,
        'create_code': create_code,
        'sales': MockSales.objects.all(),
    }

    return render(request, 'clients/client_index.html', context)


def get_details(request):
    if request.method == 'GET':
        sales_username = request.GET.get('sales_username')
        client_name = request.GET.get('client_name')
        try:
            sales = MockSales.objects.get(username=sales_username)
        except MockSales.DoesNotExist:
            return JsonResponse({'error': f'Sales {sales_username} does not exist'}, status=404)

        try:
            client = sales.clients.get(name=client_name)
        except Client.DoesNotExist:
            return JsonResponse({'error': f'Client {client_name} does not exist for Sales {sales_username}'},
                                status=404
                                )

        return JsonResponse({'name': client.name, 'information': client.information})
