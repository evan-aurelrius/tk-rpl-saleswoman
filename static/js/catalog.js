$(".sortBy").on('click', sortBy);
$("#search-button").on('click', search);

$('#search-box').keypress(function (e) {
    var key = e.which;
    if(key == 13)
     {
        $('#search-button').trigger('click'); 
     }
   });   

function search(event) {
    event.preventDefault();
    var searchText = $("#search-box").val().trim()
    $("#sort-button").html("Sort by: Product name A to Z")

    $.ajax({
        url: '/product/catalog/search/'+searchText,
        dataType: 'json',
        success: function (data) {
            if (data) {
                console.log("Success")
                $('table').empty();

                $('table').append(
                    '<thead>'+
                        '<tr>'+
                            '<th>No.</th>'+
                            '<th>Product name</th>'+
                            '<th>Product brand</th>'+
                            '<th>Product variant</th>'+
                            '<th>Product price</th>'+
                            '<th>Product stock</th>'+
                        '</tr>'+
                    '</thead>');
                
                rows = '<tbody class="table-group-divider">'
                        
                for (let i = 0; i < data.length; i++) {
                    rows += '<tr><td>'+(i+1)+'</td>'
                    rows += '<td>'+data[i].fields.name+'</td>'
                    rows += '<td>'+data[i].fields.brand+'</td>'
                    rows += '<td>'+data[i].fields.variant+'</td>'
                    rows += '<td>'+'Rp'+addDots(data[i].fields.price)+'</td>'
                    rows += '<td>'+data[i].fields.stock+'</td></tr>'
                }
                rows += '</tbody>'
                
                $('table').append(rows)
            } else {
                console.log("Netral")
            }
        },
        error: () => console.log("Error")
    });
    

}

function sortBy(event) {
    event.preventDefault();
    var btn = $(this);
    var str = btn.attr('id');
    var arr = str.split('-');
    var dynamicSortMechanism = ""
    console.log(str)
    console.log(arr[0])
    console.log(arr[1])

    $("#search-box").val("")

    if(arr[0]=='name') {
        if(arr[1]=='Asc') dynamicSortMechanism += "Product name A to Z"
        else dynamicSortMechanism += "Product name Z to A"
    }
    else if(arr[0]=='brand') {
        if(arr[1]=='Asc') dynamicSortMechanism += "Product brand A to Z"
        else dynamicSortMechanism += "Product brand Z to A"
    }
    else if(arr[0]=='price') {
        if(arr[1]=='Asc') dynamicSortMechanism += "Lowest price first"
        else dynamicSortMechanism += "Highest price first"
    }
    $("#sort-button").html("Sort by: "+dynamicSortMechanism)
    
    $.ajax({
        url: '/product/catalog/'+arr[0]+'/'+arr[1],
        dataType: 'json',
        success: function (data) {
            if (data) {
                console.log("Success")
                $('table').empty();

                $('table').append(
                    '<thead>'+
                        '<tr>'+
                            '<th>No.</th>'+
                            '<th>Product name</th>'+
                            '<th>Product brand</th>'+
                            '<th>Product variant</th>'+
                            '<th>Product price</th>'+
                            '<th>Product stock</th>'+
                        '</tr>'+
                    '</thead>');
                
                rows = '<tbody class="table-group-divider">'
                        
                for (let i = 0; i < data.length; i++) {
                    rows += '<tr><td>'+(i+1)+'</td>'
                    rows += '<td>'+data[i].fields.name+'</td>'
                    rows += '<td>'+data[i].fields.brand+'</td>'
                    rows += '<td>'+data[i].fields.variant+'</td>'
                    rows += '<td>'+'Rp'+addDots(data[i].fields.price)+'</td>'
                    rows += '<td>'+data[i].fields.stock+'</td></tr>'
                }
                rows += '</tbody>'
                
                $('table').append(rows)
            } else {
                console.log("Netral")
            }
        },
        error: () => console.log("Error")
    });

}

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