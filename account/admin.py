from django.contrib import admin
from account.models import *
# Register your models here.
admin.site.register(BaseUser)
admin.site.register(Sales)
admin.site.register(LogisticOperator)
admin.site.register(AdminUser)