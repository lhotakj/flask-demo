
window.chartColors = {
	red: 'rgb(255, 99, 132)',
	orange: 'rgb(255, 159, 64)',
	yellow: 'rgb(255, 205, 86)',
	green: 'rgb(75, 192, 192)',
	blue: 'rgb(54, 162, 235)',
	purple: 'rgb(153, 102, 255)',
	grey: 'rgb(201, 203, 207)'
};

$(document).ready(function () {

    function set_cookie(cname, cvalue, exdays=30) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }

    function del_cookie(cname) {
        set_cookie(cmame, '',-1)
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

    window.setTimeout(function () {
        $(".alert").fadeTo(500, 0).slideUp(100, function () {
            $(this).remove();
        });
    }, 5000);


    // collapsible menu
    function setMyCookie(cookie_name, is_active) {
        if (is_active == true) {
            set_cookie(cookie_name, is_active);
        } else {
            del_cookie(cookie_name);
        }
    }

    var sidenav_dom = $(".sidenav");
    var main_dom = $(".main");
    var sidenav_collapsed = get_cookie("sidenav-collapsed");

    function sidenav_expand() {
        $("i#toggler").attr("class", "fas fa-toggle-on");
        $("div.sidenav header").show()
        sidenav_dom.removeClass("sidenav-collapsed")
        main_dom.removeClass("main-collapsed")
        $("div.sidenav a").each(function (index) {
            $(this).removeClass("sidenav-a-collapsed");
        });
        $("div.sidenav a span").each(function (index) {
            $(this).removeClass("sidenav-a-span-collapsed");
        });
        $("div.main_bottom").removeClass("sidenav-a-span-collapsed");
    }

    function sidenav_collapse() {
        $("i#toggler").attr("class", "fas fa-toggle-off");
        $("div.sidenav header").hide()
        sidenav_dom.addClass("sidenav-collapsed")
        main_dom.addClass("main-collapsed")
        $("div.sidenav a").each(function (index) {
            $(this).addClass("sidenav-a-collapsed");
        });
        $("div.sidenav a span").each(function (index) {
            $(this).addClass("sidenav-a-span-collapsed");
        });
        $("div.main_bottom").addClass("sidenav-a-span-collapsed");
    }

    if (sidenav_collapsed == "1") {
        sidenav_collapse()
    }

    $("i#toggler").click(function () {
        if (sidenav_dom.hasClass('sidenav-collapsed')) {
            sidenav_expand()
            set_cookie('sidenav-collapsed','0');
            // setMyCookie("sidenav-collapsed", false);
        } else {
            sidenav_collapse()
            set_cookie('sidenav-collapsed','1');
        }
    });

//$(".alert-dismissible").fadeTo(2000, 500).slideUp(500, function(){
//    $(".alert-dismissible").alert('close');
//});

});