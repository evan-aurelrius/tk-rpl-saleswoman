from django import forms
from product.models import *

def HighlightForm() :
    product_list = Product.objects.all()
    res = []
    for i in product_list :
        pair = (i.id, i.name)
        res.append(pair)
    return res

# class HighlightForm(forms.Form):
    # product_list = forms.CharField(widget=forms.Select(choices=get_choices_product()))
