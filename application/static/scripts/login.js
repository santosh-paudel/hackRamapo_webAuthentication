$(document).ready(function (){
    $('.square').click(function () {
        var check = $(this).attr('class').split(' ').slice(-1)[0];
        $('#' + check).toggle();
    });
});

vals=[]
    $(document).on("click","#mod",function(){
      temp=$(this).css('background-color').slice(4,-1)
      vals.push(temp)
      $('#color').val(vals)
});