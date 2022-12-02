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
    
    def createAccount(self, request) :
        role = request.POST.get("role")
        if(role == "SALES") :
            full_name = request.POST.get("full-name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            role = request.POST.get("role")

            user = Sales.objects.create(
                created_account = self,
                full_name = full_name,
                email = email,
                password = password,
                role = role
            )
        else :
            full_name = request.POST.get("full-name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            role = request.POST.get("role")

            user = LogisticOperator.objects.create(
                created_account = self,
                full_name = full_name,
                email = email,
                password = password,
                role = role
            )

class LogisticOperator(BaseUser):
    created_account = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    pass 

class Sales(BaseUser):
    created_account = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    client_list = models.JSONField(null=True)
    order_list = models.JSONField(null=True)