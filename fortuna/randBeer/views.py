from django.shortcuts import render

from django.http import HttpResponse

apikey = '1ffcd2c6ba06087e62ac1a9dc1f73dfd'

from brewerydb.brewerydb import *
BreweryDb.configure(apikey)

# Create your views here.

def index(request):
	print "hello"
	print BreweryDb.beer('oeGSxs')
	# BreweryDb.beers()
	return render(request, 'index.html')

def favorites(request):
	# reponse = "You are accessing favorite beers with user %s."
	# return HttpResponse(response % user_id)
	return HttpResponse("blah favorites")

