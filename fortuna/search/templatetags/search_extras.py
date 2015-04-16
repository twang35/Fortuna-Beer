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

def searchByName(value):
	return requests.get("http://api.brewerydb.com/v2/search?type=beer&q=" + value + "&key=" + apikey +"&format=json").json()


@register.assignment_tag
def getResults(value):
    beerInfos = searchByName(value)
    if beerInfos["status"] == "success":
        if 'data' in beerInfos:
            beerData = beerInfos["data"]
            names = []
            for beerInfo in beerData:
                names.append((beerInfo['name'], beerInfo['id']))
        else: 
            return "Nothing Found"
    else:
        return ""
    return names


info = {}

@register.filter
def findBeer(value, arg):
    beerInfo = requests.get("http://api.brewerydb.com/v2/beer/" + arg + "?key=" + apikey +"&format=json").json()['data']
    if 'name' in beerInfo:
        info['name'] = beerInfo['name']
    if 'name' in beerInfo['style']['category']:
        info['style'] = beerInfo['style']['category']['name']
    if 'abv' in beerInfo:
        info['abv'] = beerInfo['abv']
    if 'description' in beerInfo:
        info['description'] = beerInfo['description']
    if 'labels' in beerInfo:
        info['labels'] = beerInfo['labels']['medium']
    else:
        info['labels'] = "../../static/images/defaultImage.png"
    return ""

@register.filter
def getName(value):
    if 'name' in info:
        return info['name']
    else:
        return ''

@register.filter
def getStyle(value):
    if 'style' in info:
        return info['style']
    else:
        return ''

@register.filter 
def getAbv(value):
    if 'abv' in info:
        return "ABV: " + info['abv'] + "%"
    else:
        return ''

@register.filter 
def getDescription(value):
    if 'description' in info:
        return info['description']
    else:
        return ''

@register.filter 
def getLabel(value):
    if 'labels' in info:
        return info['labels']
    else:
        return "../../static/images/defaultImage.png"
