$(".btnToView").click(function() {
    var btn = $(this);
    var str = btn.attr('id');
    id = str.slice(8);
    $.ajax({
        url: '/order/details/'+id,
        dataType: 'json',
        success: function (data) {
            if (data) {
                console.log("Success")
                console.log(data)
                order = data    
                temp_data = []
                list_product = order.product_list
                console.log(list_product)

                $('#orderModalLabel').text(order.pk);
                $('#orderClient').text(": "+order.client);
                $('#orderPrice').text(": Rp"+addDots(order.price));
                $('#p').text(": ");
                document.getElementById('orderProductList').innerHTML = ""
                htmlDoc = " <ol>";
                for(const [key, value] of Object.entries(list_product)){
                    htmlDoc += `
                    <li>${key} (${value})</li>
                    `
                }
                htmlDoc += "</ol>"
                document.getElementById('orderProductList').innerHTML = htmlDoc
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
