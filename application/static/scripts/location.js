$(document).ready(function() {

 	$.getJSON('//ipinfo.io/json', function(data) {
  		console.log(data)
  		$.ajax({
 	 	type:"POST",
 	 	url: '/location',
 	 	data: JSON.parse(JSON.stringify(data)),
 	 	dataType:'json',
 	 	success:function(user_loc)
 	 	{
            //Temporary function untill location is implemented in database
              if(user_loc.planet)
              {
                  $("#unknown_location").text('unknown').show()
                  $("#known_location").hide()
              }
              else{
                  
                  $("#known_location").text(user_loc.city).show()
                  $("unknown_location").hide()
              }
 	 	}
 	 });

	});

});