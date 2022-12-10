from django.shortcuts import render,redirect
from .models import Product
from account.models import BaseUser
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_protect

def catalog(request):
    session = request.session.get("user", None)
    if(session == None) :
        return redirect("account:login")
    
    user = BaseUser.objects.get(pk = session['id'])
    products = Product.objects.all().order_by('name').values()
    for p in products:
        p['price'] = 'Rp'+format(p['price'],',d').replace(",",".")
    return render(request, 'catalog.html', {'products':products,'role':user.role,'sortby':'Product name A to Z'})

def catalogSearch(request,searchText=''):
    if len(searchText)==0: products = Product.objects.all().order_by('name')
    else: products = Product.objects.filter(name__icontains = searchText).order_by('name')
    qs_json = serializers.serialize('json', products)
    return HttpResponse(qs_json, content_type='application/json')

def catalogSort(request,field,by):
    products = Product.objects.all()
    if by=='Asc':
        products = products.order_by(field)
    else:
        products = products.order_by('-'+field)
    qs_json = serializers.serialize('json', products)
    return HttpResponse(qs_json, content_type='application/json')
    
@csrf_protect    
def create(request):
    session = request.session.get("user", None)
    if(session == None) :
        return redirect("account:login")
    user_id = session['id']
    if user_id is None:
        return redirect('account:login')
    try:
        user = BaseUser.objects.get(id=user_id)
        if user.role != 'LOGISTIC OPERATOR' and user.role != 'OPERATOR LOGISTIK':
            return redirect('home:homepage')
    except BaseUser.DoesNotExist:
        return redirect('account:login')
    
    if request.method == 'POST':
        pname=request.POST.get('input-name',None)
        pbrand=request.POST.get('input-brand',None)
        pvariant=request.POST.get('input-variant',None)
        pprice=request.POST.get('input-price',None)
        pstock=request.POST.get('input-stock',None)
        try:
            newProduct = Product.objects.create(
                name=pname,
                brand=pbrand,
                variant=pvariant,
                price=pprice,
                stock=pstock
            )
        except:
            request.method = 'GET'
            return render (request, 'product.html', {'error':'Something went wrong! Please input a valid data.'})
        request.session['success'] = "Product '"+pname+"' has been added successfully!"
        return redirect('home:homepage')
        
    return render(request, 'product.html')

def getProductDetails(id):
    product = Product.objects.get(pk=id)
    return product

def getDetailJson(request,id):
    product = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", product), content_type="application/json")

def getProducts():
    products = list(Product.objects.all().order_by('name').values())
    return products