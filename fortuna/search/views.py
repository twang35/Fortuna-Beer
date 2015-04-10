from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import NameForm
from randBeer.forms import AuthenticateForm, UserCreateForm, BeerForm

from randBeer.models import Beer

def get_name(request):

	if request.method == 'GET':
		# create a form instance and populate it with data from the request:
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
								'next_url': '/', })
			else:
				auth_form = auth_form or AuthenticateForm()
				user_form = user_form or UserCreateForm()

				return render(request,
						'search.html',
						{'auth_form': auth_form,
						'user_form': user_form, 
						'search_form': search_form,})

	else:
		search_form = NameForm()
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
		

	return render(request, 'search.html', {'search_form': search_form})