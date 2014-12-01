/**
 * Author: Murad Gasanov.
 */

(function($) {
    $(document).ready(function(e) {
        var BASE_URL = "/",
            message = "Попробуйте ввести заново учетные данные",
            fatal_error = "Ошибка ответа от сервера",
            TIMEOUT = 2000;

        $("form.login").submit(function() {
            var password = $("input[name='password']").val(),
                login = $("input[name='login']").val();
            if ((password.length == 0) || (login.length == 0)) return false;
            $.post(BASE_URL+"login/",
                JSON.stringify({login: login, password: password}),
                function(data) {
                    if ("error" in data) {
                        if (data.error.length > 0) {
                            console.error(data.error);
                            noti({title:data.error.join(" "), message: message},  "error", TIMEOUT);
                        } else {
                            location.href = BASE_URL;
                            //location.reload();
                        }
                    } else {
                        noti({title: fatal_error, message: message},  "error", TIMEOUT);
                    }
                }, "json").fail(function (r) {
                    noti({title: "Error: "+r.status, message: r.statusText},  "error", TIMEOUT);
                });
            return false;
        });
    });
})(jQuery);