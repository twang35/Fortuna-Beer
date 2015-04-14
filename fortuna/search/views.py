from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from randBeer.forms import AuthenticateForm, UserCreateForm, BeerForm
from search.forms import NameForm
from django.contrib.auth.decorators import login_required

from randBeer.models import Beer

def get_name(request):

	search_form = NameForm(request.GET)
	if search_form.is_valid():
		searchName = search_form.cleaned_data['searchBeer']
		if request.user.is_authenticated():
			beer_form = BeerForm()
			user = request.user
			beers = Beer.objects.filter(user=user.id).order_by('-creation_date')[:5]
			return render(request,
							'search.html',
							{'user': user,
							'beers': beers, 
							'beer_form': beer_form, 
							'search_form': search_form,
							'searchName': searchName,
							'next_url': '/', })
		else:
			auth_form = auth_form or AuthenticateForm()
			user_form = user_form or UserCreateForm()
			
			return render(request,
					'search.html',
					{'auth_form': auth_form,
					'user_form': user_form, 
					'searchName': searchName,
					'search_form': search_form,})
	else:
		if request.user.is_authenticated():
			beer_form = BeerForm()
			user = request.user
			beers = Beer.objects.filter(user=user.id).order_by('-creation_date')[:5]
			return render(request,
							'search.html',
							{'user': user,
							'beers': beers, 
							'beer_form': beer_form, 
							'search_form': search_form,
							'next_url': '/', })
		else:
			auth_form = auth_form or AuthenticateForm()
			user_form = user_form or UserCreateForm()
			
			return render(request,
					'search.html',
					{'auth_form': auth_form,
					'user_form': user_form, 
					'search_form': search_form,})

