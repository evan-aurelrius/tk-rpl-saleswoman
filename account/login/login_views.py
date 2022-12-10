from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from account.models import *

from account.login.services.user_auth import *
# Create your views here.


def login(request) :
    session = request.session.get("user", None)
    if(session != None) :
        return redirect("account:homepage")
    else :
        if(request.method == "POST") :
            full_name = request.POST.get("full-name")
            password = request.POST.get("password")

            user = authentication(full_name, password)

            if(user == None) :
                messages.info(request, 'Wrong username or password')
            
            else :
                user_data = {
                    "id" : user.id,
                    "username": user.full_name,
                    "role" : user.role     
                }
                request.session['user'] = user_data

                return redirect('account:homepage')
        return render(request, "login.html")


def logout(request) :

    session = request.session.get("user", None)
    if(session != None) :
        request.session.flush()
        request.session.save()
        return redirect("account:login")
    else :
        return redirect("account:login")


def homepage(request) :
    session = request.session.get("user", None)
    if (session != None) :
        return render(request, "homepage.html")
    else :
        return redirect("account:login")