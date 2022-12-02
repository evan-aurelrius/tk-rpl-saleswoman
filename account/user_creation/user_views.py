from django.shortcuts import render, redirect
from django.contrib import messages

from account.models import *
from account.user_creation.services.create_account import *


def register_admin_account(request) :
    cookies = request.COOKIES.get("user", None) 
    if(cookies == None) :
        if(request.method == "POST") :
            admin = createAdminAccount(request)

            return redirect("account:login")
    
    return redirect("account:homepage")


def createAccount(request) :
    cookies = request.COOKIES.get("user", None)
    if(cookies != None) :
        user = BaseUser.objects.get(pk = cookies)

        if(user.role == "ADMIN") :
            if(request.method == "POST") :
                admin = AdminUser.objects.get(pk=cookies)
                admin.createAccount(request)
                return redirect("account:show-account-list")
            return render(request, "create_account.html")
        else :
            return redirect("account:homepage")

    return redirect("account:login")

def showAccountList(request) :
    cookies = request.COOKIES.get("user", None)
    if(cookies != None) :
        user = BaseUser.objects.get(pk = cookies)

        if(user.role == "ADMIN") :
            all_user = BaseUser.objects.all()
            context = {
                "list_user" : all_user
            }
            return render(request, "account_list.html", context)
        else :
            return redirect("account:homepage")

    return redirect("account:login")

def getAccount(request, id) :
    cookies = request.COOKIES.get("user", None)
    if(cookies != None) :
        user = BaseUser.objects.get(pk = cookies)

        if(user.role == "ADMIN") :
            selected_user = BaseUser.objects.get(pk=id)
            context = {
                "username" : selected_user.full_name,
                "email" : selected_user.email,
                "role": selected_user.role,

            }
            return render(request, "account_detail.html", context)
        else :
            return redirect("account:homepage")

    return redirect("account:login")
 