from django import template
from django.template.defaultfilters import stringfilter
import requests
import json

register = template.Library()


apikey = '5b3814c58c765b0d58b67d3525c4850b'

from brewerydb.brewerydb import *
BreweryDb.configure(apikey)

@register.filter
def getBeer(value):
	return value['data']['available']

def getRand():
	return requests.get("http://api.brewerydb.com/v2/beer/random?key=" + apikey +"&format=json").json()

info = {}
defaultImage = "../../static/images/defaultImage.png"

@register.filter
def getNewName(value):
	beerInfo = getRand()
	info['name'] = beerInfo['data']['name'];
	if 'style' in beerInfo['data']:
		if 'category' in beerInfo['data']['style']:
			if 'name' in beerInfo['data']['style']['category']:
				info['style'] = beerInfo['data']['style']['category']['name']
				if 'abv' in beerInfo['data']:
					info['abv'] = beerInfo['data']['abv']
					if 'description' in beerInfo['data']:
						info['description'] = beerInfo['data']['description']
						if 'labels' in beerInfo['data']:
							info['labelMedium'] = beerInfo['data']['labels']['medium']
							return "Name: " + info['name']
						else:
							info['labelMedium'] = defaultImage
							return "Name: " + info['name']

	return getNewName(value)

@register.filter
def getName(value):
	return info['name']

@register.filter
def getStyle(value):
	return "Style: " + info['style']

@register.filter 
def getAbv(value):
	return "ABV: " + info['abv'] + "%"

@register.filter 
def getDescription(value):
	return info['description']

@register.filter 
def getLabel(value):
	return info['labelMedium']
