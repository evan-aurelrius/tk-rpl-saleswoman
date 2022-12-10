$(".btnToView").click(function() {
    var btn = $(this);
    var str = btn.attr('id');
    id = str;
    $.ajax({
        url: `/account/show-account-detail/${id}`,
        dataType: 'json',
        success: function (data) {
            if (data) {
                console.log("Success")
                console.log(data)
                data = data[0]
                console.log(data.fields.role)
                $('#username').text(": "+data.fields.full_name);
                $('#email').text(": "+(data.fields.email));
                $('#role').text(": "+data.fields.role);
                console.log($('#role').text())
            }
        },
        error: () => console.log("Error")
    })

})