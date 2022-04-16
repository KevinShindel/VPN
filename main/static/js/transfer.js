$(document).ready(function () {

    $('#myTable').DataTable({
        "serverSide": true,
        "ajax": "/api_auth/transfer/?format=datatables",
        "columns": [
            {"data": "user.first_name", 'name': 'user.first_name'},
            {"data": "date"},
            {"data": "resource"},
            {"data": "traffic"},
        ]
    });

});
