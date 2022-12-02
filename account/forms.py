from django import forms
from account.models import *

class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        exclude = ("role")