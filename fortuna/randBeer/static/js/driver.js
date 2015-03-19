var slots = new Array();
slots[0] = new Array("Sweet", "Sour", "Bitter", "Salty");
slots[1] = new Array("Dark", "Light", "Clear");
slots[2] = new Array("Full Bodied", "Thin", "Aromatic");

var beers = ["Heady Topper", "Pliny the Younger", "Zombie Dust", "Good Morning", "Guinness Draught", "Samuel Adams Octoberfest", "Magic Hat #9", "Lagunitas IPA", "Bud Light", "Budweiser", "Coors Light", "Miller Light", "Busch Light", "Bud Light Lime", "Blue Ribbon", "Yuengling Traditional Lager"];

function getRandomBeer() {
	$.ajax({
		url: "/Users/Fei/Documents/Blind-Bet/fortuna/randBeer/management/commands/randBeer.py",
		type: 'POST',
		dataType: 'json',
		success: function(results){
			var name = results.response.name;
			var obj = JSON.parse(results)
			var description = results.response.description;
			$('#randomBeerInfo').append(obj.description);

		},
	    error: function(XMLHttpRequest, textStatus, errorThrown) { 
	        alert("Status: " + textStatus); alert("Error: " + errorThrown); 
	    }   
	});
}
