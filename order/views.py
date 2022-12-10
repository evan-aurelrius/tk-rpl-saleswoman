from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from .models import Order
from account.models import *
from clients.models import *
from product.models import *
from clients.models import *
import json

def product_JSON(request):
    product = Product.objects.all()
    return HttpResponse(serializers.serialize("json", product), content_type="application/json")

# def createOrder(request):
#     session = request.session.get("user", None)
    
#     if(session != None) :
#         user = Sales.objects.filter(pk = session['id']).first()
#         if(user != None) :
#             if request.method == "POST":
#                 data = json.loads(request.body)
#                 object_client = None
#                 product = {}
#                 order_price = 0
#                 if(len(data) == 1) :
#                     messages.warning(request, f"Please choose the product")
#                     return HttpResponse(status=400)
#                 for i in data :
#                     try :
#                         product_id = int(i)
#                         object_product = Product.objects.get(pk=product_id)
#                         quantity = int(data[i])
#                         product_price = object_product.price
#                         if quantity <= object_product.stock:
#                             product[object_product.name] = quantity
#                             order_price += quantity*product_price
#                             object_product.stock -= quantity
#                             object_product.save()
#                             return redirect("order:show-orders")
#                         else:
#                             messages.warning(request, f"Not enough stock for product {object_product.name}")
#                             return redirect("order:create-order")
#                     except :
#                         object_client = Client.objects.get(name=data[i])  
#                 order = Order.objects.create(
#                     client = object_client,
#                     product_list = product,
#                     price = order_price
#                 )
#                 user.order_list[order.id] = order.id
#                 user.save()
#                 return redirect("order:create-order")
#             client = Client.objects.all().filter(sales_id=session['id'])
#             context = {
#                 "client_list" : client,
#                 "role" : user.role
#             }
#             return render(request, "order.html", context)
#         else :
#             return redirect("/")
#     else :
#         return redirect("account:login")

def createOrder(request):
    session = request.session.get("user", None)
    
    if(session != None) :
        user = Sales.objects.filter(pk = session['id']).first()
        if(user != None) :
            if request.method == "POST":
                data = json.loads(request.body)
                object_client = None
                product = {}
                order_price = 0
                for i in data :
                    try :
                        product_id = int(i)
                        object_product = Product.objects.get(pk=product_id)
                        quantity = int(data[i])
                        product_price = object_product.price
                        if quantity <= object_product.stock:
                            product[object_product.name] = quantity
                            order_price += quantity*product_price
                            object_product.stock -= quantity
                            object_product.save()
                        else:
                            messages.warning(request, f"Not enough stock for product {object_product.name}")
                            return redirect("order:create-order")
                    except :
                        object_client = Client.objects.get(name=data[i])  
                order = Order.objects.create(
                    client = object_client,
                    product_list = product,
                    price = order_price
                )
                user.order_list[order.id] = order.id
                user.save()
                return redirect("order:create-order")
            client = Client.objects.all().filter(sales_id=session['id'])
            context = {
                "client_list" : client,
                "role" : user.role
            }
            return render(request, "order.html", context)
        else :
            return redirect("/")
    else :
        return redirect("account:login")

def showOrders(request):
    session = request.session.get("user", None)
    
    if(session != None) :
        sales = Sales.objects.filter(pk = session['id']).first()
        if(sales != None) :
            order_list = sales.order_list
            client = []
            total_price = []
            data = {

            }
            for i in order_list :
                res = []
                order = Order.objects.get(pk = int(i))
                temp = []
                temp.append(order)
                data[order.id] = temp
            context = {
                "data" : data,
                "role" : session['role']
            }
            return render(request, "show_order.html", context)
        else :
            return redirect("/")

    else :
        return redirect("account:login")

def getOrderJson(request,id):
    order = Order.objects.filter(pk=id)
    response_data = {}
    response_data['id'] = id
    response_data['client'] = order[0].client.name
    response_data['product_list'] = order[0].product_list
    response_data['price'] = order[0].price

    return HttpResponse(json.dumps(response_data), content_type="application/json")