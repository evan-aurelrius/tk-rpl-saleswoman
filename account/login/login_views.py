from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from account.models import *

from account.login.services.user_auth import *
# Create your views here.


def login(request) :
    cookies = request.COOKIES.get("user", None)
    if(cookies != None) :
        return redirect("account:homepage")
    else :
        if(request.method == "POST") :
            full_name = request.POST.get("full-name")
            password = request.POST.get("password")

            user = authentication(full_name, password)

            if(user == None) :
                messages.info(request, 'Wrong username or password')
            
            else :
                response = HttpResponseRedirect(reverse("account:homepage"))
                response.set_cookie("user", user.id)

                return response
        return render(request, "login.html")


def logout(request) :
    user = request.COOKIES.get("user", None)
    if(user != None) :
        response = HttpResponseRedirect(reverse("account:login"))
        response.delete_cookie("user")
        return response
    else :
        return redirect("account:login")


def homepage(request) :
    cookies = request.COOKIES.get("user", None)
    if (cookies != None) :
        user = BaseUser.objects.get(pk = cookies)
        context = {
            "username" :  user.full_name,
            "role" : user.role
        }
        return render(request, "homepage.html", context)
    else :
        return redirect("account:login")