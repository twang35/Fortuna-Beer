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

@register.filter
def getRand(value):

	return requests.get("http://api.brewerydb.com/v2/beer/oeGSxs?key=5b3814c58c765b0d58b67d3525c4850b&format=json").json()['data']['available']