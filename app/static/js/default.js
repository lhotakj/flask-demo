window.chartColors = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(201, 203, 207)'
};

var $j = jQuery.noConflict();

function auto_hide_flesh() {
    window.setTimeout(function () {
        $j(".alert").fadeTo(500, 0).slideUp(100, function () {
            $j(this).remove();
            window.auto_hide_flesh(); // in case there's more of the divs
        });
    }, 5000);
}

// -- called from DataTable code
function flesh(type, text) {
    const html = '<div class="alert alert-' + type + ' alert-dismissible fade show" role="alert" style="position:absolute;left: calc(50% + 110px);transform: translate(-50%, 0);"> <button type="button" class="close" onclick="window.auto_hide_flesh()" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>' + text + ' </div>';
    $j(".main_").prepend(html);
}

function call_api(endpoint, payload, text_success) {
    $j.ajax(endpoint, {
        type: 'POST',  // http method
        data: payload,  // data to submit
        success: function (data, status, xhr) {
            window.flesh('success', text_success)
        },
        error: function (jqXhr, textStatus, errorMessage) {
            window.flesh('warning', 'Error. ' + errorMessage)
        }
    });
}

// universal GET method
function get_api(endpoint, callback) {
    $j.ajax(endpoint, {
        type: 'GET',  // http method
        success: callback,
        error: function (jqXhr, textStatus, errorMessage) {
            window.flesh('warning', 'Error. ' + errorMessage)
        }
    });
}

$j(document).ready(function () {

    function set_cookie(cname, cvalue, exdays = 30) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }

    function del_cookie(cname) {
        set_cookie(cmame, '', -1)
    }

    function get_cookie(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }

    // collapsible menu
    function setMyCookie(cookie_name, is_active) {
        if (is_active == true) {
            set_cookie(cookie_name, is_active);
        } else {
            del_cookie(cookie_name);
        }
    }

    var sidenav_dom = $j(".sidenav");
    var main_dom = $j(".main");
    var sidenav_collapsed = get_cookie("sidenav-collapsed");

    function sidenav_expand() {
        $j("i#toggler").attr("class", "fas fa-toggle-on");
        $j("div.sidenav header").show()
        sidenav_dom.removeClass("sidenav-collapsed")
        main_dom.removeClass("main-collapsed")
        $j("div.sidenav a").each(function (index) {
            $j(this).removeClass("sidenav-a-collapsed");
        });
        $j("div.sidenav a span").each(function (index) {
            $j(this).removeClass("sidenav-a-span-collapsed");
        });
        $j("div.main_bottom").removeClass("sidenav-a-span-collapsed");
    }

    function sidenav_collapse() {
        $j("i#toggler").attr("class", "fas fa-toggle-off");
        $j("div.sidenav header").hide()
        sidenav_dom.addClass("sidenav-collapsed")
        main_dom.addClass("main-collapsed")
        $j("div.sidenav a").each(function (index) {
            $j(this).addClass("sidenav-a-collapsed");
        });
        $j("div.sidenav a span").each(function (index) {
            $j(this).addClass("sidenav-a-span-collapsed");
        });
        $j("div.main_bottom").addClass("sidenav-a-span-collapsed");
    }

    if (sidenav_collapsed == "1") {
        sidenav_collapse()
    }

    $j("i#toggler").click(function () {
        if (sidenav_dom.hasClass('sidenav-collapsed')) {
            sidenav_expand()
            set_cookie('sidenav-collapsed', '0');
            // setMyCookie("sidenav-collapsed", false);
        } else {
            sidenav_collapse()
            set_cookie('sidenav-collapsed', '1');
        }
    });

});

window.auto_hide_flesh();