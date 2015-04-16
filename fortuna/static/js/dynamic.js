$(document).ready(function(){
    $('#btnSuggestBeer').click(function(){
		var style;
		style = $('#randomBeerStyle').text();
   		$.get('/suggest/', {beerStyle: style}, function(data){
               $('#test').html(data);
    	});

	});
});

