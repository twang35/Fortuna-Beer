from django.shortcuts import render

from django.http import HttpResponse



# Create your views here.

def suggest(request):
	# reponse = "You are accessing favorite beers with user %s."
	# return HttpResponse(response % user_id)
	return render(request, 'suggest.html')

