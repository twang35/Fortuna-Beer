from django.shortcuts import render
from django import template
from django.http import HttpResponse
from random import randrange
import requests
import json
from django.http import JsonResponse

register = template.Library()

apikey = '5b3814c58c765b0d58b67d3525c4850b'

from brewerydb.brewerydb import *
BreweryDb.configure(apikey)

# Create your views here.

def suggest(request):
	# reponse = "You are accessing favorite beers with user %s."
	# return HttpResponse(response % user_id)
	return render(request, 'suggest.html')

def getSuggestion(request):
	# reponse = "You are accessing favorite beers with user %s."
	# return HttpResponse(response % user_id)
	
	if request.method == 'GET':
		style = request.GET['beerStyle']
		beerInfos = searchByStyle(style)
		totalResults = beerInfos['totalResults']
		random = randrange(0, 30)
		if 'data' in beerInfos:
			beerData = beerInfos["data"][random]
			return JsonResponse(beerData)
           
        else: 
			result = "Nothing Found"
			return HttpResponse(result)
           
		
	return HttpResponse(random)

def searchByStyle(value):
	return requests.get("http://api.brewerydb.com/v2/search?type=beer&q=" + value + "&key=" + apikey +"&format=json").json()