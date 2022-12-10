from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'information']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Client Name'}),
            'information': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Client Information'}),
        }
