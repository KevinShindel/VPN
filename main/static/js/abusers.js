$(document).ready(function () {

    $("#show_report").click(function () {
        let query = $("#report_date option:selected")
        let title = query.text() + ' Abusers report'
        let month = query.val()
        $("#modal_title").text(title)

        $('#myTable').DataTable({
            serverSide: false,
            ajax: {
                url: "/abusers/report/",
                contentType: 'application/json',
                data: {
                    'month': month
                },
                dataType: 'json',
            },
            "destroy": true,
            "searching": false,
            "paging": false,
            "columns": [
                {"data": "name"},
                {"data": "traffic"},
                {"data": "quote"},
            ]
        });
    });

    $("#generate_report").click(function () {
        $.ajax({
            url: "/abusers/generate/",
            type: "GET",
            data: {},
            success: function () {
                alert('Data have been generated!')
            },
            error: function () {
                alert('Bad!')
            }

        })
    })
});
