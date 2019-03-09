$.ajax({
    type: "GET",
    url: "get_chart_data",
    dataType: "json",
    astnc: true,
    // data: { csrfmiddlewaretoken: '{#{ csrf_token }#}' },
    success: function(data) {
        $('#output').html(data.message);
        data(data.message);
    }
    // context: data
});
// .done(function (response) {
//     // $(this).addClass("done");
//     // console.log(data);
//     alert(response);
//     console.log(response);
// });