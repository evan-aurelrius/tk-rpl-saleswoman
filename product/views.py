from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from account.models import BaseUser
from django.http import HttpResponse
from django.core import serializers

def catalog(request):
    user_id = request.COOKIES.get('user', None)
    if user_id is None:
        return redirect('account:login')
    
    user = BaseUser.objects.get(pk = user_id)
    products = Product.objects.all()
    for p in products:
        p.price = 'Rp'+format(p.price,',d').replace(",",".")
    return render(request, 'catalog.html', {'products':products,'role':user.role})
    
def create(request):
    user_id = request.COOKIES.get('user', None)
    if user_id is None:
        return redirect('account:login')
    try:
        user = BaseUser.objects.get(id=user_id)
        if user.role != 'LOGISTIC OPERATOR' and user.role != 'OPERATOR LOGISTIK':
            return redirect('home:index')
    except BaseUser.DoesNotExist:
        return redirect('account:login')
    
    if request.method == 'POST':
        pname=request.POST.get('input-name',None)
        pbrand=request.POST.get('input-brand',None)
        pvariant=request.POST.get('input-variant',None)
        pprice=request.POST.get('input-price',None)
        pstock=request.POST.get('input-stock',None)
        
        newProduct = Product.objects.create(
            name=pname,
            brand=pbrand,
            variant=pvariant,
            price=pprice,
            stock=pstock
        )
        return redirect('home:index')
        
    return render(request, 'product.html')

def getProductDetails(id):
    product = Product.objects.get(pk=id)
    return product

def getDetailJson(request,id):
    product = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", product), content_type="application/json")

def getProducts():
    products = list(Product.objects.all())
    return products