from account.models import BaseUser
from django.core.exceptions import *

def authentication(full_name, password) :
    user = None
    try :
        user = BaseUser.objects.get(full_name = full_name)
        if(user.password != password) :
            user = None
            pass
    except ObjectDoesNotExist :
        pass
    return user
