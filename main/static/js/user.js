$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})


$(document).ready(function () {
    let userId = $('#user_id');
    let company = $('#company')


    let table = $('#myTable').DataTable({
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
    $('#save').click(()=> {
        let method = 'POST';
        let url = `/api_auth/user/`;


        if ($('#save').attr('data-action') === 'edit') {
            method = 'PUT';
            url += `${userId}.val()}/`
        }
        $.ajax({
            type: method,
            url: url,
            data: {
                'first_name': $('#first_name').val(),
                'last_name': $('#last_name').val(),
                'email': $('#email').val(),
                'company': $('#company').val(),
                'id': userId.val(),
            },
            dataType: 'json',
            success: ()=> {
                $("#exampleModal").modal("hide");
                table.ajax.reload();
            }
        })
    });

    $('#add_user').on('click', ()=> {
        $('#save').attr('data-action', 'add');
        $('#first_name').val('');
        $('#last_name').val('');
        $('#email').val('');
        $('#company').val('');
        userId.val('');
        $('#modal_title').text('ADD');
        $("#exampleModal").modal("show");
    });

    // EDIT
    table.on('click', '#edit', ()=> {
        $('#save').attr('data-action', 'edit');
        let data = table.row($(this).parents('tr')).data();
        $('#first_name').val(data['first_name']);
        $('#last_name').val(data['last_name']);
        $('#email').val(data['email']);
        company.val(data['company.id']);
        company.text(data['company.name']);
        userId.val(data['id']);
        $('#modal_title').text('EDIT');
        $("#exampleModal").modal("show");
    });

    // DELETE
    table.on('click', '#remove', ()=> {
        let data = table.row($(this).parents('tr')).data();
        $.ajax({
            type: 'DELETE',
            url: `/api_auth/user/${data['id']}`,
            data: {},
            dataType: 'json',
            success: ()=> {
                table.ajax.reload();
            }
        })
    });

    let options = [];

    company.find('option').each(function () {
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
