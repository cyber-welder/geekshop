window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;
        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            },
        })
    });

    $('.product-button').on('click', 'button[action="add"]', function () {
        var t_href = event.target;
        $.ajax({
            url: '/baskets/add/' + t_href.name + '/',
            success: function (data) {
                $('.product-button button[name="' + t_href.name + '"]').parent().html(data.result);
            },
        })
    });

    $('.product-button').on('click', 'button[action="remove"]', function () {
        var t_href = event.target;
        $.ajax({
            url: '/baskets/remove/' + t_href.name + '/',
            success: function (data) {
                $('.product-button button[name="' + t_href.name + '"]').parent().html(data.result);
            },
        })
    });

}
