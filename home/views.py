from django.shortcuts import render,redirect
from product.views import getProducts
from account.models import BaseUser

def index(request):
    session = request.session.get("user", None)
    success = request.session.get("success", "")
    if(session == None) :
        return redirect("account:login")
    
    user = BaseUser.objects.get(pk = session['id'])
    products = getProducts()
    context = {
        'products':products,
        'role':user.role
    }
    if success: 
        context['success'] = success
        del request.session['success']
    return render(request, 'home.html', context)