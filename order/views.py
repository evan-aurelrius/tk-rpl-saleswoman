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

def createOrder(request):
    cookies = request.COOKIES.get("user", None)
    client = Client.objects.all()
    if(cookies != None) :
        user = Sales.objects.filter(pk = int(cookies)).first()
        if(user != None) :
            if request.method == "POST":
                data = json.loads(request.body)
                object_client = None
                product = {}
                order_price = 0
                print(data)
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
                user.client_list[object_client.id] = object_client.name
                user.order_list[order.id] = order.id
                user.save()
                return redirect("order:create-order")
            context = {
                "client_list" : client
            }
            return render(request, "order.html", context)
        else :
            return redirect("account:homepage")
    else :
        return redirect("account:login")

def showOrders(request):
    cookies = request.COOKIES.get("user", None)
    if(cookies != None) :
        sales = Sales.objects.filter(pk = int(cookies)).first()
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
                temp.append(order.id)
                temp.append(order.price)
                temp.append(order.client.name)
                data[order.id] = temp
            context = {
                "data" : data
            }
            return render(request, "show_order.html", context)
        else :
            return redirect("account:homepage")

    else :
        return redirect("account:login")

def getOrder(request, id):
    cookies = request.COOKIES.get("user", None)
    if(cookies != None) :
        sales = Sales.objects.filter(pk=int(cookies)).first()
        if(sales != None) :
            order_list = sales.order_list
            client = []
            total_price = []
            data = {

            }
            for i in order_list :
                res = []
                if(i == id) :
                    order = Order.objects.get(pk = int(i))
                    print(order)
                    for j in order.product_list :
                        res.append(j)
                    temp = []
                    temp.append(res)
                    temp.append(order.price)
                    temp.append(order.client.name)
                    data[order.id] = temp
                    break
            context = {
                "data" : data
            }
            return render(request, "show_order_detail.html", context)
        else :
            return redirect("account:homepage")
    else :
        return redirect("account:login")