from django import template
from django.template.defaultfilters import stringfilter
import requests
import json

register = template.Library()


apikey = '1ffcd2c6ba06087e62ac1a9dc1f73dfd'

from brewerydb.brewerydb import *
BreweryDb.configure(apikey)

@register.filter
def getBeer(value):
	return value['data']['available']

def getRand():
	return requests.get("http://api.brewerydb.com/v2/beer/random?key=5b3814c58c765b0d58b67d3525c4850b&format=json").json()
	
beerInfo = getRand()


@register.filter
def getName(value):
	if 'name' in beerInfo['data']:
		return beerInfo['data']['name']
	return ''

@register.filter
def getStyle(value1):
	if 'style' in beerInfo['data']:
		if 'category' in beerInfo['data']['style']:
			if 'name' in beerInfo['data']['style']['category']:
				return beerInfo['data']['style']['category']['name']
	return ''

@register.filter 
def getAbv(value):
	if 'abv' in beerInfo['data']:
		return beerInfo['data']['abv']
	return ''

@register.filter 
def getDescription(value):
	global beerInfo
	if 'description' in beerInfo['data']:
		foo = beerInfo['data']['description']
		beerInfo = getRand()
		return foo
	beerInfo = getRand()
	return ''
