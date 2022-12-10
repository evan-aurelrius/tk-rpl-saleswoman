from django.urls import path
from account.login.login_views import *
from account.user_creation.user_views import *


app_name = 'account'

urlpatterns = [
    path("register/", register_admin_account, name="register-admin"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("create-account/", createAccount, name="create-account"),
    path("show-account-list/", showAccountList, name="show-account-list" ),
    path("show-account-detail/<id>", getAccount, name="show-account-detail" ),


]