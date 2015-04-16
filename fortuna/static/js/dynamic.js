$(document).ready(function(){
    $('#btnRandBeer').click(function(){
		var name;
		name = $('#randomBeerStyle').html()
   		$.get('/suggest/', {beerName: name}, function(data){
               $('#test').html(data);
    	});

	});
});

