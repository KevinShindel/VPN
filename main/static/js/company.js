$(document).ready(function () {
    var editor;
    var url_path = '/api_auth/company/';
    editor = new $.fn.dataTable.Editor({
        ajax: {
            create: {
                type: "POST",
                dataSrc: "",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                url: url_path,
                data: function (d) {
                    var newdata;
                    $.each(d.data, function (key, value) {
                        newdata = JSON.stringify(value);
                    });
                    return newdata;
                },
                success: function (data) {
                    $('#myTable').DataTable().ajax.reload();
                },
            },
            edit: {
                type: "PUT",
                url: url_path + "_id_/",
                dataSrc: "",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: function (d) {
                    var newdata;
                    $.each(d.data, function (key, value) {
                        newdata = JSON.stringify(value);
                    });
                    return newdata;
                },
                success: function (data) {
                    $('#myTable').DataTable().ajax.reload();
                },
            },
            remove: {
                type: "DELETE",
                url: url_path + "_id_/",
                dataSrc: "",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: function (d) {
                    var newdata;
                    $.each(d.data, function (key, value) {
                        newdata = JSON.stringify(value);
                    });
                    return newdata;
                },
                success: function (data) {
                    $('#myTable').DataTable().ajax.reload();
                },
            }
        },
        table: '#myTable',
        idSrc: 'id',
        fields: [
            {label: 'Name', name: 'name'},
            {label: 'Quote', name: 'quote'},
        ]

    });

    var table = $('#myTable').DataTable({
        "serverSide": true,
        "ajax": "/api_auth/company/?format=datatables",
        dom: 'Bfrtip',
        "columns": [
            {"data": "name"},
            {"data": "quote"},
        ],
        select: true,
        buttons: [
            {extend: 'create', editor: editor},
            {extend: 'edit', editor: editor},
            {extend: 'remove', editor: editor}
        ]
    });
});
