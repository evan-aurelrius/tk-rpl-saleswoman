from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponseRedirect
from django.contrib import messages

from account.models import *

from services.user_auth import *
# Create your views here.


def login(request) :
    cookies = request.COOKIES.get("user", None)
    if(cookies != None) :
        return redirect("account:home")
    else :
        if(request.method == "POST") :
            full_name = request.POST.get("username")
            password = request.POST.get("password")
            
            user = authentication(full_name, password)

            if(user == None) :
                messages.info(request, 'Wrong username or password')
            
            else :
                response = HttpResponseRedirect(reverse("account:homepage"))
                response.set_cookie("user", user)

                return response
        return render(request, "login.html")


def logout(request) :
    
    user = request.COOKIES.get("user", None)
    if(user != None) :
        request.COOKIES.delete("user")
        return HttpResponseRedirect(reverse("account:login"))
    else :
        return redirect("account:login")
