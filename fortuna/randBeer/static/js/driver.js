var slots = new Array();
slots[0] = new Array("Sweet", "Sour", "Bitter", "Salty");
slots[1] = new Array("Dark", "Light", "Clear");
slots[2] = new Array("Full Bodied", "Thin", "Aromatic");

var beers = ["Heady Topper", "Pliny the Younger", "Zombie Dust", "Good Morning", "Guinness Draught", "Samuel Adams Octoberfest", "Magic Hat #9", "Lagunitas IPA", "Bud Light", "Budweiser", "Coors Light", "Miller Light", "Busch Light", "Bud Light Lime", "Blue Ribbon", "Yuengling Traditional Lager"];

// function pull() {
// 	for (var i = 0; i < slots.length; i++) {
// 		document.getElementById('slot'+(i+1)).innerHTML = slots[i][Math.floor(Math.random()*slots[i].length)];
// 	}
// 	randBeer();
// }

// function randBeer() {
// 	document.getElementById('chosen_one').innerHTML = beers[Math.floor(Math.random()*beers.length)];
// }

// function getRandomBeer() {
//     $.get( 
//           'http://api.brewerydb.com/v2/beer/random?key=0975ed5b18f4fb7e0de63b3e84fdd17a'
//        ).success(function(resp){
//             document.getElementById('randomBeerInfo').innerHTML = resp;
//        });
// }

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
