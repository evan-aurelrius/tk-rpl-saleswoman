from django.urls import path
from account.login.login_views import *
from account.user_creation.user_views import *


app_name = 'account'

urlpatterns = [
    path("register/", register_admin_account, name="register-admin"),
    path("login/", login, name="login"),
    path("logout/", login, name="logout"),
    path("create-account/", login, name="create-account"),
    path("home/", login, name="home"),


]