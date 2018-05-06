$(function () {
    $('#give').hover(function() {
        $(this).animate({'opacity':0.3}, 1000, 'swing', function () {
        })
    },function () {
        $(this).animate({'opacity':1}, 1000, 'swing', function () {
        })
    });
});

