from django.shortcuts import render,redirect
from product.views import getProducts
from account.models import BaseUser

def index(request):
    session = request.session.get("user", None)
    if(session == None) :
        return redirect("account:login")
    
    user = BaseUser.objects.get(pk = session['id'])
    products = getProducts()
    return render(request, 'home.html',{'products':products,'role':user.role})