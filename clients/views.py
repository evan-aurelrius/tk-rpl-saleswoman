from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError

from account.models import Sales
from clients.forms import ClientForm
from clients.models import Client


def create_client(request):
    sales_id = request.COOKIES.get('user', None)
    if sales_id is None:
        return redirect('account:login')

    try:
        sales = Sales.objects.get(id=sales_id)
    except Sales.DoesNotExist:
        return redirect('account:homepage')

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                sales.create_client(form.cleaned_data['name'], form.cleaned_data['information'])
                request.session['create_code'] = 1
            except IntegrityError:
                request.session['create_code'] = 0

            return redirect('client_index')
        else:
            request.session['create_code'] = 0
            return redirect('client_index')

    return redirect('client_index')


def index(request):
    sales_id = request.COOKIES.get('user', None)
    if sales_id is None:
        return redirect('account:login')

    try:
        sales = Sales.objects.get(id=sales_id)
    except Sales.DoesNotExist:
        return redirect('account:homepage')

    form = ClientForm()
    create_code = -1
    if 'create_code' in request.session:
        create_code = request.session['create_code']
        del request.session['create_code']

    context = {
        'form': form,
        'create_code': create_code,
        'sales': sales,
        'role': sales.role,
    }

    return render(request, 'clients/client_index.html', context)


def get_details(request):
    sales_id = request.COOKIES.get('user', None)
    if sales_id is None:
        return JsonResponse({'error': f'Please login first'}, status=401)

    try:
        sales = Sales.objects.get(id=sales_id)
    except Sales.DoesNotExist:
        return JsonResponse({'error': f'Please login as Sales'}, status=403)

    if request.method == 'GET':
        client_name = request.GET.get('client_name')

        try:
            client = sales.clients.get(name=client_name)
        except Client.DoesNotExist:
            return JsonResponse(
                {'error': f'Client {client_name} does not exist for Sales {sales.full_name}'}, status=404
            )

        return JsonResponse({'name': client.name, 'information': client.information})
