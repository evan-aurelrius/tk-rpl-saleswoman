from account.models import *

def createAdminAccount(request) :
    user = None
    role = request.POST.get("role")
    if(role == "ADMIN") :
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        user = AdminUser.objects.create(
            full_name = full_name,
            email = email,
            password = password,
            role = role
        )
    user.save()
    return user


def createAccount(request, admin) :
    user = None
    if(role == "SALES") :
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        user = Sales.objects.create(
            created_account = admin,
            full_name = full_name,
            email = email,
            password = password,
            role = role
        )
    else :
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        user = LogisticOperator.objects.create(
            created_account = admin,
            full_name = full_name,
            email = email,
            password = password,
            role = role
        )
    user.save()
    return user