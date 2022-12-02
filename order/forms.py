from django import forms
from .models import Order
# from client.models import *
from product.models import *

# clients = Client.objects.all
# CHOICES_CLIENTS = clients
# result1 = []
# for i in CHOICES_CLIENTS :
#      pair = (i.name, i.id)
#      result1.append(pair)
# CHOICES_CLIENTS = result1

def show_choiches_product():
    products = Product.objects.all()
    CHOICES_PRODUCT = products
    result2 = []
    for i in CHOICES_PRODUCT :
        pair = (i.id, i.name)
        result2.append(pair)
    CHOICES_PRODUCT = result2
    return CHOICES_PRODUCT

class OrderForm(forms.Form):
    # client = forms.CharField(widget=forms.Select(choices=CHOICES_CLIENT))
    product_list = forms.MultipleChoiceField(choices=show_choiches_product(), widget=forms.CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs) :
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['product_list'] = forms.MultipleChoiceField(choices=show_choiches_product(), widget=forms.CheckboxSelectMultiple())