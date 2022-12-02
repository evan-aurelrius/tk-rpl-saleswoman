from django.shortcuts import render, redirect
from django.contrib import messages

from account.models import *
from account.user_creation.services.create_account import *


def register_admin_account(request) :

    if(request.method == "POST") :
        admin = createAdminAccount(request)

        return redirect("account:login")
    
    return render("account:register-admin")


def create_sales_account(request) :
    cookies = request.COOKIES.get("user", None)
    if(cookies != None) :
        user = BaseUser.objects.get(pk = cookies)

        if(user.roles == "ADMIN") :
            if(request.method == "POST") :
                sales = createAccount(request, user)
                return redirect("account:show_account_list")
        else :
            return redirect("account:home")

    return redirect("account:login")


def create_logistic_operator_account(request) :
    cookies = request.COOKIES.get("user", None)
    if(cookies != None) :
        user = BaseUser.objects.get(pk = cookies)
        
        if(user.roles == "ADMIN") :
            if(request.method == "POST") :
                logistic_operator = createAccount(request, user)
                return redirect("account:show_account_list")
        else :
            return redirect("account:home")

    return redirect("account:login")