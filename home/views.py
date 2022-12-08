from django.shortcuts import render,redirect
from product.views import getProducts
from account.models import BaseUser

def index(request):
    user_id = request.COOKIES.get('user', None)
    if user_id is None:
        return redirect('account:login')
    user = BaseUser.objects.get(pk = user_id)
    products = getProducts()
    return render(request, 'home.html',{'products':products,'role':user.role})