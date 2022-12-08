from account.models import *

def createAdminAccount(request) :
    user = None
    full_name = request.POST.get("full-name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    role = "ADMIN"

    user = AdminUser.objects.create(
        full_name = full_name,
        email = email,
        password = password,
        role = role
    )
    user.save()
    return user
