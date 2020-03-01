$(document).ready(function () {


window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(100, function(){
        $(this).remove();
    });
}, 5000);

//$(".alert-dismissible").fadeTo(2000, 500).slideUp(500, function(){
//    $(".alert-dismissible").alert('close');
//});

});