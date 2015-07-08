$(function() {
    // Topbar active tab support
    $(".topbar li").removeClass("active");

    var class_list = $("body").attr("class").split(/\s+/);
    $.each(class_list, function(index, item) {
        var selector = "ul.nav li#tab_" + item;
        $(selector).addClass("active");
    });

    $("#account_logout, .account_logout").click(function(e) {
        e.preventDefault();
        $("#accountLogOutForm").submit();
    });
});


