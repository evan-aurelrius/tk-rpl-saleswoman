from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from account.models import BaseUser,Sales

def index(request):
    user_id = request.COOKIES.get('user', None)
    if user_id is None:
        return redirect('account:login')
    
    form = ProductForm
    if request.method == 'POST':
        try:
            user = BaseUser.objects.get(id=user_id)
            if user.role != 'SALES':
                return redirect('account:homepage')
        except BaseUser.DoesNotExist:
            return redirect('account:homepage')
        
        friendForm = ProductForm(request.POST)
        if friendForm.is_valid():
            friendForm.save()
            return redirect('product:index')
        
    products = Product.objects.all
    return render(request, 'product.html', {'form':form,'products':products})

def getProductDetails(id):
    product = Product.objects.get(pk=id)
    return product

