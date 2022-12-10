from django.shortcuts import render


from .models import *
from product.views import *
from .forms import *

def create_highlight(request) :
    session = request.session.get("user", None)
    if(session == None) :
        return redirect("account:login")
    
    user = BaseUser.objects.get(pk = session['id'])
    
    form = HighlightForm()

    if (request.method == "POST") :
        form = HighlightForm(request.POST)
        if(form.is_valid()) :
            selected_product = form.cleaned_data['product_list']
            highlight = Highlight.objects.all().first()
            if(highlight == None) :
                Highlight.objects.create()
                highlight = Highlight.objects.all().first()
            if(highlight.highlight_product.get(selected_product) == None) :
                object_product = Product.objects.get(pk = int(selected_product))
                highlight.highlight_product[selected_product] = object_product.name
                highlight.save()
    
    context = {
        "form" : form,
        "role" : user.role
    }

    return render(request, "create_highlight.html", context)

def show_highlight(request) :
    session = request.session.get("user", None)
    if(session == None) :
        return redirect("account:login")
    
    user = BaseUser.objects.get(pk = session['id'])
    
    highlight_objects = list(Highlight.objects.all())
    res = []
    for i in highlight_objects :
        for j in i.highlight_product:
            res.append(getProductDetails(int(j)))
    context = {"highlight_list":res,"role":user.role}
    return render(request, "show_highlight.html", context)
        
