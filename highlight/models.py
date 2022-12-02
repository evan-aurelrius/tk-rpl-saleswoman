from django.db import models
from django.contrib.auth.models import User
from product.models import *

class Highlight(models.Model):
    highlight_product = models.JSONField(null=True, default=dict)