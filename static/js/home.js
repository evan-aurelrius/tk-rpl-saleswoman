$(".btnToView").click(function() {
    var btn = $(this);
    var str = btn.attr('id');
    id = str.slice(8);
    
    $.ajax({
        url: '/product/details/'+id,
        dataType: 'json',
        success: function (data) {
            if (data) {
                console.log("Success")
                product = data[0]
                console.log(product.fields.name)
                $('#productModalLabel').text(product.fields.name);
                $('#productPrice').text(": Rp"+addDots(product.fields.price));
                $('#productBrand').text(": "+product.fields.brand);
                $('#productVariant').text(": "+product.fields.variant);
                $('#productStock').text(": "+product.fields.stock);
            } else {
                console.log("Netral")
            }
        },
        error: () => console.log("Error")
    })

})

function addDots(nStr) {
    nStr += '';
    x = nStr.split('.');
    x1 = x[0];
    x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + '.' + '$2'); // changed comma to dot here
    }
    return x1 + x2;
}