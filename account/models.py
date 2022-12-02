from django.db import models

ROLE_CHOICES = (
    ("ADMIN", "ADMIN"),
    ("OPERATOR LOGISTIK", "OPERATOR LOGISTIK"),
    ("SALES", "SALES")
)

# Create your models here.
class BaseUser(models.Model) :
    full_name = models.CharField(max_length=100, unique=True)   
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

class AdminUser(BaseUser):
    pass

class LogisticOperator(BaseUser):
    created_account = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    pass 

class Sales(BaseUser):
    created_account = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    client_list = models.JSONField(null=True)
    order_list = models.JSONField(null=True)