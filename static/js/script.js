function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// Use csrf token while doing post request, this will prevent 500 Server Error
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

//All Books API
$.ajax({
    url: "http://localhost:8000/api/books/",
    dataType: "json",
    success: function (response) {
        let trHTML = '';
        $.each(response, function (i, item) {
            trHTML += "<tr><th>" + item.id + "</th><td>" + item.title + "</td><td>" + item.category + "</td><td>" + item.author + "</td><td>" + item.price + "</td><td> <button class='btn btn-warning update btn-sm' id =" + item.id + " data-toggle='modal' data-target='#editBook'><i class='bi bi-pencil-square'></i> Update</button> <button class='btn btn-danger btn-sm delete' id =" + item.id + " data-toggle='modal' data-target='#deleteBook'><i class='bi bi-trash'></i> Delete</button>"
            "</td></tr>";
        });
        $('#Book-Records').append(trHTML);
    }
});

$('#create').click(function () {
    $("#add-Book").trigger('reset');
});

//Save New Book Button
$(function () {
    $('#addBook').on('submit', function (e) {
        e.preventDefault();

        let myurl = "http://localhost:8000/api/books/add/";

        $.ajax({
            type: 'POST',
            url: myurl,
            data: $("#addBook :input").serializeArray(),
            dataType: "json",
            success: function (data) {
                alert("Book Added!");
                location.reload();
            },
            error: function (data) {
                alert("Book Not Added!");
                location.reload();
            }
        });
    });
});

//Edit Books API
$('#Book-Records').on('click', '.update', function (e) {
    e.preventDefault();

    let id = $(this).attr('id');
    $('input[id=Myid]').val(id);

    let myurl = "http://localhost:8000/api/books/" + id + "/";

    $("#b-title").change(function () {
        $('input[name=title]').val($(this).val());
    });
    $("#b-category").change(function () {
        $('select[name=category]').val($(this).val());
    });
    $("#b-author").change(function () {
        $('input[name=author]').val($(this).val());
    });
    $("#p-price").change(function () {
        $('input[name=price]').val($(this).val());
    });

    $.ajax({
        async: true,
        url: myurl,
        method: 'GET',
        success: function (result) {
            $('input[name="title"]').val(result.title);
            $('select[name="category"]').val(result.category);
            $('input[name="author"]').val(result.author);
            $('input[name="price"]').val(result.price);
        }
    });

});

//Save Edited Book Button
$(function () {
    $('#editBook').on('submit', function (e) {
        e.preventDefault();

        let id = $("#Myid").attr("value");
        console.log(id);

        let myurl = "http://localhost:8000/api/books/edit/" + id + "/";

        $.ajax({
            type: 'PUT',
            url: myurl,
            data: $("#editBook :input").serializeArray(),
            dataType: "json",
            success: function (data) {
                alert("Book Updated!");
                location.reload();
            },
            error: function (data) {
                alert("Book Not Updated!");
                location.reload();
            }
        });
    });
});

//Delete Books API
$('#Book-Records').on('click', ".delete", function (e) {
    e.preventDefault();

    let id = $(this).attr('id');
    $('input[id=Myid]').val(id);
    console.log(id)

    let myurl = "http://localhost:8000/api/books/" + id + "/";

    $.ajax({
        async: true,
        url: myurl,
        method: 'GET',
        success: function (result) {
            $('input[name="id"]').val(result.id);
        }
    });

});

//Save Delete Books Button
$(function () {
    $('#deleteBook').on('submit', function (e) {
        e.preventDefault();

        let id = $("#Myid").attr("value");
        console.log(id);

        let myurl = "http://localhost:8000/api/books/delete/" + id + "/";

        $.ajax({
            async: true,
            url: myurl,
            method: 'DELETE',
            headers: {"X-Requested-With": "XMLHttpRequest"},
            success: function (result) {
                location.reload();
            },
            error: function (result) {
                alert("Book Not Deleted!");
                location.reload();
            }
        });

    });
});   