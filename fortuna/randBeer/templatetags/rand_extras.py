from django import template
from django.template.defaultfilters import stringfilter
import requests
import json

register = template.Library()


apikey = '1ffcd2c6ba06087e62ac1a9dc1f73dfd'

from brewerydb.brewerydb import *
BreweryDb.configure(apikey)

@register.filter
@stringfilter
def getBeer(value, args):
	return BreweryDb.beer(value)

def getRand():
	return requests.get("http://api.brewerydb.com/v2/beer/random?key=5b3814c58c765b0d58b67d3525c4850b&format=json").json()
	
beerInfo = getRand()


@register.filter
def getName(value):
	return beerInfo['data']['name']

@register.filter
def getStyle(value1):
	return beerInfo['data']['style']['category']['name']

@register.filter 
def getAbv(value):
	return beerInfo['data']['abv']

@register.filter 
def getDescription(value):
	return beerInfo['data']['description']