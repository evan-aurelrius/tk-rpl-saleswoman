from django.shortcuts import render,redirect


from .models import *
from product.views import *
from .forms import *

def create_highlight(request) :
    form = HighlightForm()

    if (request.method == "POST") :
        form = HighlightForm(request.POST)
        if(form.is_valid()) :
            selected_product = form.cleaned_data['product_list']
            highlight = Highlight.objects.all().first()
            if(highlight == None) :
                Highlight.objects.create()
                highlight = Highlight.objects.all().first()
            # if(len(highlight) == 0) :
            #     create_highlight = Highlight.object.create()
            #     highlight = Highlight.objects.all()
            if(highlight.highlight_product.get(selected_product) == None) :
                object_product = Product.objects.get(pk = int(selected_product))
                highlight.highlight_product[selected_product] = object_product.name
                highlight.save()
    
    context = {
        "form" : form
    }

    return render(request, "cart.html", context)

def show_highlight(request) :
    highlight_objects = list(Highlight.objects.all())
    res = []
    for i in highlight_objects :
        for j in i.highlight_product:
            res.append(getProductDetails(int(j)))
    context = {"highlight_list":res}
    return render(request, "show_highlight.html", context)
        
