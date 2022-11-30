from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

def index(request):
    form = ProductForm
    if request.method == 'POST':
        friendForm = ProductForm(request.POST)
        if friendForm.is_valid():
            friendForm.save()
            return redirect('product')
    products = Product.objects.all
    return render(request, 'product.html', {'form':form,'products':products})

def getProductDetails(id):
    product = Product.objects.get(pk=id)
    return product