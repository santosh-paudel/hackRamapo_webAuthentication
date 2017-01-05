vals = []
$(document).ready(function (){
    $('.square').click(function () {
        var check = $(this).attr('class').split(' ').slice(-1)[0],
            temp = $(this).css('background-color').slice(4,-1),
            index = inArray(temp);
        
        // toggle the green check
        $('#' + check).toggle();
        
        if (index === -1) {
            vals.push(temp)
        } else {
            vals.splice(index, 1);
        }
        $('#color').val(vals);
    });
    
    // forgot password modal
    $("#forgot_password").click(function(){
        $("#forgotPassword").modal({backdrop: true});
    });
    
    $('#resetPwdForm').submit( function(e) {
        var form = $(this);
        console.log($('#resetEmail').val());
        e.preventDefault();

        data = {
            'email': $('#resetEmail').val()
        }
        
        $.ajax({
            type: form.attr('method'),
            data: JSON.stringify(data, null, '\t'),
            contentType: 'application/json;charset=UTF-8',
            url: form.attr('action'),
            success: function(data){
                if (data == "success") {
                    console.log("yas");
                    $("#forgotPassword").modal('hide');
                    $('#success').modal({backdrop: true});
                }  
            }
        });
    });
});

// check if the color is already in the array
function inArray(color){
    for (var i = 0; i < vals.length; i++){
        if (vals[i] == color){
            return i;
        }
    }
    return -1;
}