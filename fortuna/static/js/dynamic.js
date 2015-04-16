$(document).ready(function(){
    $('#btnSuggestBeer').click(function(){
		var style;
		style = $('#randomBeerStyle').text();
   		$.get('/suggest/', {beerStyle: style}, function(data){
               $('#test').html(data);
    	});
   	});

    $('#btnRandBeer').click(function(){
		var name;
		name = $('#randomBeerStyle').html()

		$.ajax({
		  url: 'http://54.172.157.49/proxy.php',
		  dataType: 'jsonp',
		  success: function(json){
		    $('#randomBeerName').html( 'Name: '+json.data.name );
		    $('#randomBeerStyle').html( 'Style: '+json.data.style.category.name );
		    $('#randomBeerAbv').html( 'ABV: '+json.data.abv );
		    $('#randomBeerDescription').html( 'Description: '+json.data.description );
		    $('#randomBeerLabel').html( '<img src="' + json.data.labels.medium + '" alt="Beer Label" class = "pull-right" width = "100%">');

		  }
		});
	});
});
