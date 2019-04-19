$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})


$(document).ready(function () {

    var table = $('#myTable').DataTable({
        serverSide: true,
        ajax: {
            url: "/api_auth/user/?format=datatables",
            contentType: 'application/json',
        },
        columns: [
            {"data": "first_name"},
            {"data": "last_name"},
            {"data": "email"},
            {"data": "company_name"},
            {
                "data": null,
                "defaultContent": '<button type="button" id="edit" data-id="id" class="btn btn-warning">Edit</button>' + '&nbsp;&nbsp' +
                    '<button type="button" id="remove" class="btn btn-danger">Remove</button>'
            }
        ],
    });

    // SAVE
    $('#save').click(function () {
        var method = 'POST';
        var url = `/api_auth/user/`;

        if ($('#save').attr('data-action') === 'edit') {
            method = 'PUT';
            url += `${$('#user_id').val()}/`
        }
        $.ajax({
            type: method,
            url: url,
            data: {
                'first_name': $('#first_name').val(),
                'last_name': $('#last_name').val(),
                'email': $('#email').val(),
                'company': $('#company').val(),
                'id': $('#user_id').val(),
            },
            dataType: 'json',
            success: function (data) {
                $("#exampleModal").modal("hide");
                table.ajax.reload(null, false);
            }
        })
    });

    $('#add_user').on('click', function () {
        $('#save').attr('data-action', 'add');
        $('#first_name').val('');
        $('#last_name').val('');
        $('#email').val('');
        $('#company').val('');
        $('#user_id').val('');
        $('#modal_title').text('ADD');
        $("#exampleModal").modal("show");
    });

    // EDIT
    table.on('click', '#edit', function (event) {
        $('#save').attr('data-action', 'edit');
        var data = table.row($(this).parents('tr')).data();
        $('#first_name').val(data['first_name']);
        $('#last_name').val(data['last_name']);
        $('#email').val(data['email']);
        $('#company').val(data['company.id']);
        $('#company').text(data['company.name']);
        $('#user_id').val(data['id']);
        $('#modal_title').text('EDIT');
        $("#exampleModal").modal("show");
    });

    // DELETE
    table.on('click', '#remove', function (event) {
        var data = table.row($(this).parents('tr')).data();
        $.ajax({
            type: 'DELETE',
            url: `/api_auth/user/${data['id']}`,
            data: {},
            dataType: 'json',
            success: function (data) {
                table.ajax.reload(null, false);
            }
        })
    });

    var options = [];

    $('#company').find('option').each(function () {
        options.push($(this).val());
    });

    $('#random').click(function () {
        $('#first_name').val(faker.name.firstName());
        $('#last_name').val(faker.name.lastName());
        $('#email').val(faker.internet.email());
        let random = Math.floor(Math.random() * options.length);
        $('#company').val(options[random]);
    });
});
