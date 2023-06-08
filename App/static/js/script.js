/* --------------------------------------------------
#  All scripts here it will extends to all the pages 
----------------------------------------------------*/
// 1) If no staff, show the message
$(document).ready(function() {
    var verify = $("#chk_td").length;
        if (verify == 0) {
            $("#no-data").text("No staff found");
        }
});

// 2) time running at real time
setInterval(function() {
    var date = new Date();
    $("#clock").html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" + (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);

// 3) Validate add <inputs>
function validateEmail(email) {
    var regex = /^([a-zA-Z0-9.+_-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function validateAll()  {
    var title = $("#title").val();
    var first_name = $("#first_name").val();
    var last_name = $("#last_name").val(); 
    var mobile = $("#mobile").val();
    var card_id_no = $("#card_id_no").val();  
    var birthdate = $("#birthdate").val();       
    var age = $("#age").val();
    var gender = $("#gender").val(); 
    var bloodgrp = $("#bloodgrp").val();    
    var email = $("#email").val();
    var address = $("#address").val();    


    if (title=='') {
        swal("Opsss !","Title field cannot be empty.","error")
        return false;
    }

    /*---firstname can't be uppercase--------------
    else if (first_name==first_name.toUpperCase()) {
        swal("Opsss !","FirstName field cannot be uppercase.","error")
        $("#first_name").val();
        return false;
    }
    ---------------------------------------------*/

    else if (first_name=='') {
        swal("Opsss !","FirstName field cannot be empty.","error")
        return false;
    }



    else if (last_name=='') {
        swal("Opsss !","LastName field cannot be empty.","error")
        return false;
    }
    else if (mobile=='') {
        swal("Opsss !","เบอร์โทรศัพท์ field cannot be empty.","error")
        return false;
    } 
    else if (card_id_no=='') {
        swal("Opsss !","บัตรประจำตัว ปชช. field cannot be empty.","error")
        return false;
    }

    else if (birthdate=='' ^ null) {
        swal("Opsss !","วัน-เดือน-ปร เกิด field cannot be empty.","error")
        $("#birthdate").val("");        
        return false;
    }    

    else if (age=='') {
        swal("Opsss !","อายุ field cannot be empty.","error")
        $("#age").val("");        
        return false;
    }

    else if (bloodgrp=='') {
        swal("Opsss !","กรุ๊ปเลือด field cannot be empty.","error")
        return false;
    }
    
    else if (gender=='') {
        swal("Opsss !","เพศ field cannot be empty.","error")
        return false;
    }
    else if (email=='') {
        swal("Opsss !","Email Address field cannot be empty.","error")
        return false;
    }  
    else if (!(validateEmail(email))){
        swal("Opsss !","Put a valid Email address.","error")
        $("#email").val("");
        return false;
    }     
    else if (address=='') {
        swal("Opsss !","ที่อยู่ field cannot be empty.","error")
        return false;
    }
    else {
        return true;
    }
}
$("#btn-add").bind("click",validateAll);

// 4) Script  - Only letters is allowed
$(document).ready(function() {
    jQuery('input[first_name="first_name').keyup(function() {
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Z _]/g, '');
        jQuery(this).val(allow);
    });
    // Prevent starting with space
    $("input").on("keypress"), function(e) {
        if (e.which === 32 && !this.value.length)
        e.preventDefault();
    };
});

// 5) Only the first and last name(prevent fullname)
/*-------------------------------------------------
$(document).ready(function() {
    $("#first_name").keyup(function() {
        var first_name = $("first_name").val();
        if (first_name.split('').length == 3) {
            swal("Opsss !","Only Name and Last name..","info");
            $('#first_name').val("");
            return false;
        }
    })
});
-------------------------------------------------*/
// 6) First letter capitalized (First name and Last name)
/*---------------------------------------------------
$("#first_name").keyup(function() {
        var txt = $(this).val();
        $(this).val(txt.replace(/^(.)|\s(.)/g, function($1) {
            return $1.toUpperCase();
        }))
});
---------------------------------------------------*/

// 7) Phone mask (inputmask)
$(document).ready(function() {
    $("#mobile").inputmask("(999) 999-9999",{"onincomplete": function() {
        swal("Opsss !","incomplete phone. Please review !","info");
        return false;
        }
    });
});

// 8) Script to LOWERCASE <input> email
$(document).ready(function() {
    $("#email").keyup(function() {
        this.value = this.value.toLowerCase();
        return false;
    });
});

// 9) If AGE has number greater than 110,auto clear (second method)
$(document).ready(function() {
    $("#age").keyup(function() {
        var age =$("#age").val();
        if (age > 110) {
            swal("Denied !","the maximum value is 110 years old !","error");
            $("#age").val("");
            return false;
        }
    });
});

// 10) Script to allow only numbers in AGE
$("#age").keyup(function() {
    if (!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9]/).join('');
    }
});

// 11) Prevent starting by zeor in AGE field
$("#age").on("input", function() {
    if (/^0/.test(this.value)) {
        this.value = this.value.replace(/^0/,"")
    }
})

// 12) Script to allow only numbers in CARD_ID_NO
$("#card_id_no").keyup(function() {
    if (!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9]/).join('');
    }
});


