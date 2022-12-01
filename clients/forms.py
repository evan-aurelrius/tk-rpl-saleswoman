from django import forms
from .models import Client, MockSales


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'sales': forms.Select(choices=MockSales.objects.all().values_list('id', 'username'))
        }

