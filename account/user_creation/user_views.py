from django.shortcuts import render, redirect
from django.contrib import messages

from account.models import *
from account.user_creation.services.create_account import *


def register_admin_account(request) :
    session = request.session.get("user", None) 
    if(session == None) :
        if(request.method == "POST") :
            admin = createAdminAccount(request)

            return redirect("account:login")
        return render(request, "register.html")
    
    return redirect("account:homepage")


def createAccount(request) :
    session = request.session.get("user", None)
    if(session != None) :
        user = BaseUser.objects.get(pk = session['id'])
        if(user.role == "ADMIN") :
            if(request.method == "POST") :
                admin = AdminUser.objects.get(pk=session['id'])
                admin.createAccount(request)
                return redirect("account:show-account-list")
            return render(request, "create_account.html")
        else :
            return redirect("account:homepage")

    return redirect("account:login")

def showAccountList(request) :
    session = request.session.get("user", None)
    if(session != None) :
        user = BaseUser.objects.get(pk = session['id'])

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
    session = request.session.get("user", None)
    if(session != None) :
        user = BaseUser.objects.get(pk = session['id'])

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
 