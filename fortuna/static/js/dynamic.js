$(document).ready(function(){
    $('#btnSuggestBeer').click(function(){
		var style;
		style = $('#randomBeerStyle').text();
   		$.get('/suggest/', {beerStyle: style}, function(data){
			beerName = data.name;
			beerStyle = data.style;
			beerAbv = data.abv;
			beerDescription = data.description;
            $('#suggestName').html("<strong>" + beerName + "<strong>");
			$('#suggestDescription').html(beerDescription);
    	});
   	});

    $('#btnRandBeer').click(function(){
		var name;
		name = $('#randomBeerStyle').html()

		$.ajax({
		  url: 'http://54.172.157.49/proxy.php',
		  dataType: 'jsonp',
		  success: function(json){
		    $('#randomBeerName').html( json.data.name );
		    
		    if(json.data.hasOwnProperty('style')) {
		    	$('#randomBeerStyle').html( 'Style: '+json.data.style.category.name );
		    }
		    else {
		    	$('#randomBeerStyle').html( 'Style: missing' );
		    }
		    
		    if(json.data.hasOwnProperty('abv')) {
		    	$('#randomBeerAbv').html( 'ABV: '+json.data.abv );
		    }
		    else {
		    	$('#randomBeerAbv').html( 'ABV: missing');
		    }
		    
		    if(json.data.hasOwnProperty('description')) {
		    	$('#randomBeerDescription').html( 'Description: '+json.data.description );
		    }
		    else {
		    	$('#randomBeerAbv').html( 'Description: missing');
		    }
		    
		    if(json.data.hasOwnProperty('labels')){
			    $('#randomBeerLabel').html( '<img src="' + json.data.labels.medium + '" alt="Beer Label" class = "pull-right" width = "100%">');
			}
			else {
				$('#randomBeerLabel').html( '<img src="../../static/images/defaultImage.png" alt="Beer Label" class = "pull-right" width = "100%">');
			}
		    $('input[name=beer_name]').val(json.data.name);
		  }
		});
	});
});
