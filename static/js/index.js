/**
 * Created by Murad
 */

$(document).ready(function (e) {

    var BASE_URL = "/";

    var TIMEOUT = 3000;

    var GLOBAL_OPTIONS = {
        query: "",
        start_width: false,
        sort_by_name: true
    };

    var MESSAGE = {
        wait: "Загрузка...",
        error: "Ошибка: "
    };

    kendo.culture("ru-RU");

    $("#tabstrip").kendoTabStrip({
        animation: {
            open: {
                effects: "fadeIn"
            }
        }
    });

    var controller = $("#controller").kendoGrid({
        dataSource: {
            type: "json",
            transport: {
                read: {
                    url: BASE_URL + "controller/read/",
                    dataType: "json",
                    type: "POST"
                },
                destroy: {
                    url: BASE_URL + "controller/destroy/",
                    dataType: "json",
                    type: "POST"
                },
                parameterMap: function (options, operation) {
                    if (operation !== "read" && options) {
                        return {item: kendo.stringify(options)};
                    }
                }
            }
//            schema: {
//                model: {
//                    id: "subdivision_id",
//                    fields: { name: {type: "string"}, tel: {type: "string"} }
//                }
//            },
//            requestEnd: function (e) {
//                if (e.type == "destroy") {
//                    $reload_author.click();
//                }
//                n.close();
//            }
        },
//        toolbar: [
//            { template: kendo.template($("#subdivision_header_template").html()) }
//        ],
        height: 600,
        sortable: true,
        editable: {
            mode: "inline",
            confirmation: "Вы уверены, что хотите удалить запись?",
            confirmDelete: "Да",
            cancelDelete: "Нет"
        },
        columns: [
        ]
    }).data("kendoGrid");

    window_option.width = 500;
    var subdivision_window = $("#change_subdivision_window").kendoWindow(window_option).data("kendoWindow");
    var subdivision_model = kendo.observable({
        subdivision_id: 0,
        name: "",
        tel: ""
    });
    var $change_subdivision = $("#change_subdivision");
    kendo.bind($change_subdivision, subdivision_model);
    var subdivision_validator = $change_subdivision.kendoValidator(validator_option).data("kendoValidator");

    $(".add_subdivision").click(function (e) {
        $(".k-widget.k-tooltip.k-tooltip-validation.k-invalid-msg").hide();
        $("#is_subdivision_edit").val(false);
        subdivision_model.set("subdivision_id", 0);
        subdivision_model.set("name", "");
        subdivision_model.set("tel", "");
        subdivision_window.center().open();
    });

    $("#subdivision_cancel").click(function (e) {
        subdivision_window.close();
        return false;
    });

    function check_response_subdivision(d) {
        var data = subdivision.dataSource;
        var item = data.get(d.subdivision_id);
        if (item) {
            item.name = d.name;
            item.tel = d.tel;
        } else {
            item = {
                subdivision_id: d.subdivision_id,
                name: d.name,
                tel: d.tel
            };
            data.add(item);
        }
        n.close();
        subdivision.refresh();
        subdivision_window.close();
    }

    $("#subdivision_save").click(function (e) {
        if (!subdivision_validator.validate()) return false;
        var send = {
            subdivision_id: subdivision_model.get("subdivision_id"),
            name: subdivision_model.get("name"),
            tel: subdivision_model.get("tel")
        };
        n = noty_message(M_SAVE, false);
        if ($("#is_subdivision_edit").val() === "false") {
            $.post(BASE_URL + API_BASE_URL + "subdivision/create/",
                {item: JSON.stringify(send) }, check_response_subdivision, "json");
        } else {
            $.post(BASE_URL + API_BASE_URL + "subdivision/update/",
                {item: JSON.stringify(send) }, check_response_subdivision, "json");
        }
        return false;
    });

});