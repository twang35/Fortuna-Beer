from django.shortcuts import render

from django.http import HttpResponse



# Create your views here.

def index(request):
	return render(request, 'index.html')

def favorites(request):
	# reponse = "You are accessing favorite beers with user %s."
	# return HttpResponse(response % user_id)
	return HttpResponse("blah favorites")

