from django import template
from django.template.defaultfilters import stringfilter
import requests

register = template.Library()


apikey = '1ffcd2c6ba06087e62ac1a9dc1f73dfd'

from brewerydb.brewerydb import *
BreweryDb.configure(apikey)

@register.filter
@stringfilter
def getBeer(value, args):
	return BreweryDb.beer(value)

@register.filter
def getRand(value):
	return requests.get("http://api.brewerydb.com/v2/beer/random?key=5b3814c58c765b0d58b67d3525c4850b&format=json").json()