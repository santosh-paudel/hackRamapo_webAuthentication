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